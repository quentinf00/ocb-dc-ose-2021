import json
import logging
import operator
from functools import partial
from pathlib import Path

import aprl.part
import aprl.utils
import hydra_zen
import xarray as xr
from ocn_tools._src.metrics.stats import nrmse_ds

_log = logging.getLogger(__name__)


def mu(
    study_paths: str = "data/prepared/method_output/map_on_track.nc",
    ref_paths: str = "data/prepared/ref/default.nc",
    output_path: str = "data/metrics/mu.json",
    preprocess_ref=None,
    preprocess_study=None,
):
    r"""

    Compute the normalized RMSE score:

    .. math::
        \mu =  1 - \frac{RMS(ref - study)}{RMS(ref)}

    Args:
        output_path (str): Path where to write the json with the score value
        preprocess_ref (xr.Dataset -> xr.DataArray): Preprocessing that returns the reference DataArray
        preprocess_study (xr.Dataset -> xr.DataArray): Preprocessing that returns the analysis DataArray
        study_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the analysis dataset
        ref_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the reference dataset
    """
    _log.info("Starting")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    _log.debug(f"Opening {study_paths=}")
    _log.debug(f"Applying preprocessing {preprocess_study}")
    _log.debug(f"{getattr(preprocess_study, '__doc__', '')}")
    study_da = xr.open_mfdataset(
        study_paths, preprocess=preprocess_study, combine="nested", concat_dim="time"
    )

    _log.debug(f"Opening {ref_paths=}")
    _log.debug(f"Applying preprocessing {preprocess_ref}")
    _log.debug(f"{getattr(preprocess_ref, '__doc__', '')}")
    ref_da = xr.open_mfdataset(
        ref_paths, preprocess=preprocess_ref, combine="nested", concat_dim="time"
    )

    eval_ds = xr.Dataset(dict(study=study_da, ref=ref_da)).load()

    partial_score_fn = partial(
        nrmse_ds,
        target="study",
        reference="ref",
        dim=["time"],
    )

    mu = eval_ds.pipe(partial_score_fn).item()

    _log.info(f"Mu score: {mu}")
    _log.debug(f"Writing to : {output_path}")

    with open(Path(output_path), "w") as f:
        json.dump({"$\mu$": mu}, f)
    _log.info("Done")


_b = hydra_zen.make_custom_builds_fn()
run, cfg = aprl.part.register(
    mu,
    base_args=dict(
        preprocess_ref=_b(aprl.utils.kw2a, fn=operator.itemgetter, ssh_var="ssh"),
        preprocess_study=_b(aprl.utils.kw2a, fn=operator.itemgetter, ssh_var="rec_ssh"),
    ),
)

if __name__ == "__main__":
    run()
