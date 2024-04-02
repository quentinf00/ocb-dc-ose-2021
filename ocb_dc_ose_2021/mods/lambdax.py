import json
import logging
import operator
from functools import partial
from pathlib import Path

import aprl.module
import hydra_zen
import numpy as np
import xarray as xr
from ocn_tools._src.metrics.power_spectrum import psd_welch_score
from ocn_tools._src.preprocessing.alongtrack import select_track_segments

log = logging.getLogger(__name__)


def min_intersect(ds, threshold=0.5, dvar="score", dim="wavenumber"):
    max_wnx = ds.isel(**{dim: ds[dvar] <= threshold})[dim].min().item()
    log.debug(
        f"not considering above {max_wnx:.2f}, score: {ds.sel(**{dim: max_wnx})[dvar]:.2f}"
    )
    intersect = (
        ds.isel(**{dim: ds[dim] <= max_wnx})
        .swap_dims(**{dim: dvar})
        .interp({dvar: threshold})[dim]
        .item()
    )
    return intersect


def lambdax(
    study_paths: str = "data/prepared/method_output/map_on_track.nc",
    ref_paths: str = "data/prepared/ref/default.nc",
    delta_t: float = 0.9434,
    velocity: float = 6.77,
    length_scale: float = 1000,
    segment_overlapping: float = 0.25,
    output_lambdax_path="data/metrics/lambdax.json",
    output_psd_path="data/method_outputs/psd_score.nc",
    preprocess_ref=None,
    preprocess_study=None,
):
    log.info("Starting")
    study_da = xr.open_mfdataset(
        study_paths, preprocess=preprocess_study, combine="nested", concat_dim="time"
    )
    ref_da = xr.open_mfdataset(
        ref_paths, preprocess=preprocess_ref, combine="nested", concat_dim="time"
    )

    eval_ds = xr.Dataset(dict(study=study_da, ref=ref_da)).load()
    eval_ds = eval_ds.where(eval_ds.ref.pipe(np.isfinite), drop=True).interpolate_na(
        dim="time", method="nearest"
    )
    delta_x = velocity * delta_t

    partial_track_fn = partial(
        select_track_segments,
        variable_interp="study",
        variable="ref",
        velocity=velocity,
        delta_t=delta_t,
        length_scale=length_scale,
        segment_overlapping=segment_overlapping,
    )

    partial_score_fn = partial(
        psd_welch_score,
        variable="study",
        variable_ref="ref",
        delta_x=delta_x,
        nperseg=length_scale // delta_x,
    )

    segments = eval_ds.pipe(partial_track_fn)
    ds, _ = segments.pipe(partial_score_fn)

    ## Robust lambda_x computation when small wavelength reach score > 0.5
    lambda_x = 1 / min_intersect(ds)
    log.info(f"Effective scale resolved (interpolated at score 0.5) {lambda_x:.2f}")

    Path(output_lambdax_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_psd_path).parent.mkdir(parents=True, exist_ok=True)
    ds.to_netcdf(output_psd_path)
    with open(Path(output_lambdax_path), "w") as f:
        json.dump({"$\lambda_x$": lambda_x}, f)
    log.info("Done")


b = hydra_zen.make_custom_builds_fn()
run, cfg = aprl.module.register(
    lambdax,
    base_args=dict(
        preprocess_ref=b(aprl.utils.kw2a, fn=operator.itemgetter, ssh_var="ssh"),
        preprocess_study=b(aprl.utils.kw2a, fn=operator.itemgetter, ssh_var="rec_ssh"),
    ),
)

if __name__ == "__main__":
    run()
