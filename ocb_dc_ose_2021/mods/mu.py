import json
import logging
import operator
from functools import partial
from pathlib import Path

import aprl.module
import hydra_zen
import xarray as xr
from ocn_tools._src.metrics.stats import nrmse_ds

log = logging.getLogger(__name__)


def mu(
    study_paths: str = "data/prepared/method_output/map_on_track.nc",
    ref_paths: str = "data/prepared/ref/default.nc",
    output_path: str = "data/metrics/mu.json",
    preprocess_ref=None,
    preprocess_study=None,
):
    log.info("Starting")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    study_da = xr.open_mfdataset(
        study_paths, preprocess=preprocess_study, combine="nested", concat_dim="time"
    )
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

    log.info(f"Mu score: {mu}")
    log.debug(f"Writing to : {output_path}")

    with open(Path(output_path), "w") as f:
        json.dump({"$\mu$": mu}, f)
    log.info("Done")


b = hydra_zen.make_custom_builds_fn()
mu_endpoint, mu_cfg = aprl.module.register(
    mu,
    base_args=dict(
        preprocess_ref=b(operator.itemgetter, "ssh"),
        preprocess_study=b(operator.itemgetter, "rec_ssh"),
    ),
)

if __name__ == "__main__":
    mu_endpoint()
