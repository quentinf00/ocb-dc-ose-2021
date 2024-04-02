import glob
from functools import partial
from pathlib import Path

import aprl.module
import aprl.utils
import hydra_zen
import ocn_tools._src.geoprocessing.validation as ocnval
import pandas as pd
import xarray as xr


def preprocess_track(
    ds,
    min_lon: float = -66,
    max_lon: float = -54,
    min_lat: float = 32,
    max_lat: float = 44,
    min_time: str = "2016-12-01",
    max_time: str = "2018-02-01",
):
    return (
        ds.rename(longitude="lon", latitude="lat")
        .pipe(ocnval.validate_latlon)
        .pipe(ocnval.validate_time)
        .pipe(
            lambda d: d.where(
                (d.lon.load() >= min_lon)
                & (d.lon <= max_lon)
                & (d.lat.load() >= min_lat)
                & (d.lat <= max_lat)
                & (d.time.load() >= pd.to_datetime(min_time))
                & (d.time <= pd.to_datetime(max_time)),
                drop=True,
            )
        )
        .assign(ssh=lambda d: d.sla_filtered + d.mdt - d.lwe)
        .pipe(ocnval.validate_ssh)
        .sortby("time")[["ssh"]]
    )


def prepare_track(input_paths, output_path, preprocess):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    xr.open_mfdataset(
        input_paths,
        preprocess=preprocess,
        combine="nested",
        concat_dim="time",
    ).to_netcdf(output_path)


def sorted_glob(pathname):
    return sorted(glob.glob(pathname=pathname, recursive=True))


b = hydra_zen.make_custom_builds_fn(populate_full_signature=True)
pb = hydra_zen.make_custom_builds_fn(zen_partial=True, populate_full_signature=True)

run, cfg = aprl.module.register(
    prepare_track,
    base_args=dict(
        input_paths=b(sorted_glob, pathname="data/downloads/ref/**/*.nc"),
        output_path="data/prepared/ref/default.nc",
        preprocess=pb(
            preprocess_track,
            min_lon=-65,
            max_lon=-55,
            min_lat=33,
            max_lat=43,
            min_time="2017-01-01",
            max_time="2017-12-31",
        ),
    ),
)

if __name__ == "__main__":
    run()
