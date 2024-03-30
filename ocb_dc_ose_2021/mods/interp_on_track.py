from functools import partial
from pathlib import Path

import aprl.module
import hydra_zen
import ocn_tools._src.geoprocessing.gridding as ocngri
import ocn_tools._src.geoprocessing.validation as ocnval
import xarray as xr


def preprocess_map(ds, ssh_var="ssh"):
    return (
        ds.pipe(ocnval.validate_latlon)
        .pipe(ocnval.validate_time)
        .pipe(partial(ocnval.validate_ssh, variable=ssh_var))[[ssh_var]]
    )


def interp_on_track(
    grid_paths, track_paths, output_path, preprocess_grid=None, preprocess_track=None
):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    map = xr.open_mfdataset(
        grid_paths, preprocess=preprocess_grid, combine="nested", concat_dim="time"
    )
    track = xr.open_mfdataset(
        track_paths, preprocess=preprocess_track, combine="nested", concat_dim="time"
    )
    ocngri.grid_to_coord_based(src_grid_ds=map, tgt_coord_based_ds=track).to_netcdf(
        output_path
    )


b = hydra_zen.make_custom_builds_fn(populate_full_signature=True)
run, cfg = aprl.module.register(
    interp_on_track,
    base_args=dict(
        grid_paths="???",
        track_paths="data/prepared/ref/default.nc",
        output_path="data/prepared/method_output/map_on_track.nc",
        preprocess_grid=partial(preprocess_map, ssh_var="rec_ssh"),
        preprocess_track=None,
    ),
)

if __name__ == "__main__":
    run()
