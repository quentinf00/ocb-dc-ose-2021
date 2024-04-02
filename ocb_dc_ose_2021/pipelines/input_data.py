import aprl.pipeline

import ocb_dc_ose_2021.mods.cmems_get as cmems_get
import ocb_dc_ose_2021.mods.prepare_track as prepare_track

dataset_id_cfg = cmems_get.cfg.dataset_id
regex_cfg = cmems_get.cfg.regex
_01_dl_track = cmems_get.cfg(
    dataset_id=dataset_id_cfg(sat="${...params.sat}"),
    regex=regex_cfg(
        min_time="${...params.min_time}",
        max_time="${...params.max_time}",
    ),
    download_dir="${...params.dl_dir}/${.sat}",
)

input_paths_cfg = prepare_track.input_paths
preprocess_cfg = prepare_track.preprocess
_02_prepare_track = prepare_track.cfg(
    input_paths=input_paths_cfg(
        pathname="${..._01_dl_track.download_dir}",
    ),
    preprocess=preprocess_cfg(
        min_lon="${...params.min_lon}",
        max_lon="${...params.max_lon}",
        min_lat="${...params.min_lat}",
        max_lat="${...params.max_lat}",
        min_time="${...params.min_time}",
        max_time="${...params.max_time}",
    ),
    output_path="${...params.output_dir}/${.._01_dl_track.sat}.nc",
)
stages = {
    "_01_dl_track": _01_dl_track,
    "_02_filter_tracks": _02_prepare_track,
}


params = dict(
    sweep=None,
    sat_list=["alg", "h2ag", "j2g", "j2n", "j3", "s3a"],
    dl_dir="data/downloads/input",
    output_dir="data/prepared/input",
    min_time="2016-12-01",
    max_time="2018-02-01",
    min_lon=-66.0,
    max_lon=-54.0,
    min_lat=32.0,
    max_lat=44.0,
)

sweep = {
    "params.sweep": dict(
        _target_="builtins.str.join", _args_=[",", "${params.sat_list}"]
    )
}

pipeline, recipe, params = aprl.pipeline.register(
    "dc_ose_2021_inference_data", stages=stages, params=params, default_sweep=sweep
)
