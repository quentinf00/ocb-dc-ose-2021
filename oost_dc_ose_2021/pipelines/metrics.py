"""
## Overview:
Download and prepare the reference data for SSH Mapping evaluation (requires CMEMS credentials for download)
Filter and compute ssh ("sla_filtered + mdt - lwe")
Interpolate ssh reconstruction on interpolated track
Compute effective resolution of the alongtrack reconstruction
Compute nrmse_score of the alongtrack reconstruction


## Basic Usage:
  * `oost-dc_ose_2021-metrics params.study_path=<path_to_rec.nc>` to run full pipeline (reference data download, preparation to metrics)
  * `oost-dc_ose_2021-metrics to_run=[_03_interp_on_track,_04_1_lambdax,_04_2_mu] params.study_path=<path_to_rec.nc>` to run only metric computation with available ref data
  *  `oost-dc_ose_2021-metrics params.(min|max)_(lon|lat|time)=<bound>` to change the bound
  *  `oost-dc_ose_2021-metrics -cd conf overrides=my_conf` to load config from conf/aprl/overrides/my_conf.yaml

## Params:
  * method: label of the method used for naming files
  * study_path: path to the netcdf dataset to evaluate
  * study_var: variable of the netcdf to use
  * sat: altimeter id to download
  * min_time: start of the temporal domain
  * max_time: end of the temporal domain
  * min_lon: lower longitudinal bound
  * max_lon: upper longitudinal bound
  * min_lat: upper latitudinal bound
  * max_lat: upper latitudinal bound
"""

import aprl.appareil

import oost_dc_ose_2021.mods.cmems_get as cmems_get
import oost_dc_ose_2021.mods.interp_on_track as interp_on_track
import oost_dc_ose_2021.mods.lambdax as lambdax
import oost_dc_ose_2021.mods.mu as mu
import oost_dc_ose_2021.mods.prepare_track as prepare_track

_dataset_id_cfg = cmems_get.cfg.dataset_id
_regex_cfg = cmems_get.cfg.regex
_cmems_get_cfg = aprl.utils.make_partial(cmems_get.cfg)
_01_dl_track = _cmems_get_cfg(
    dataset_id=_dataset_id_cfg(sat="${....params.sat}"),
    regex=_regex_cfg(
        min_time="${....params.min_time}",
        max_time="${....params.max_time}",
    ),
    output_directory="data/downloads/ref/${...params.sat}",
)

_input_paths_cfg = prepare_track.cfg.input_paths
_preprocess_cfg = prepare_track.cfg.preprocess
_prepare_track_cfg = aprl.utils.make_partial(prepare_track.cfg)
_02_prepare_track = _prepare_track_cfg(
    input_paths=_input_paths_cfg(
        pathname="${..._01_dl_track.output_directory}/**/*.nc",
    ),
    preprocess=_preprocess_cfg(
        min_lon="${....params.min_lon}",
        max_lon="${....params.max_lon}",
        min_lat="${....params.min_lat}",
        max_lat="${....params.max_lat}",
        min_time="${....params.min_time}",
        max_time="${....params.max_time}",
    ),
    output_path="data/prepared/ref/${...params.sat}.nc",
)

_interp_on_track_cfg = aprl.utils.make_partial(interp_on_track.cfg)
_preprocess_map_cfg = interp_on_track.cfg.preprocess_grid
_03_interp_on_track = _interp_on_track_cfg(
    grid_paths="${...params.study_path}",
    preprocess_grid=_preprocess_map_cfg(ssh_var="${....params.study_var}"),
    track_paths="${.._02_prepare_track.output_path}",
    output_path="data/prepared/method_outputs/${...params.method}_on_track.nc",
)

_lambdax_cfg = aprl.utils.make_partial(lambdax.cfg)
_pp_lx_study_cfg = lambdax.cfg.preprocess_study
_pp_lx_ref_cfg = lambdax.cfg.preprocess_ref
_04_1_lambdax = _lambdax_cfg(
    ref_paths="${.._02_prepare_track.output_path}",
    study_paths="${.._03_interp_on_track.output_path}",
    output_lambdax_path="data/metrics/lambdax_${...params.method}.json",
    output_psd_path="data/prepared/method_outputs/psd_${...params.method}.nc",
    preprocess_study=_pp_lx_study_cfg(ssh_var="${....params.study_var}"),
    preprocess_ref=_pp_lx_ref_cfg(ssh_var="ssh"),
)

_mu_cfg = aprl.utils.make_partial(mu.cfg)
_pp_mu_study_cfg = mu.cfg.preprocess_study
_pp_mu_ref_cfg = mu.cfg.preprocess_ref
_04_2_mu = _mu_cfg(
    ref_paths="${.._02_prepare_track.output_path}",
    study_paths="${.._03_interp_on_track.output_path}",
    output_path="data/metrics/mu_${...params.method}.json",
    preprocess_study=_pp_mu_study_cfg(ssh_var="${....params.study_var}"),
    preprocess_ref=_pp_mu_ref_cfg(ssh_var="ssh"),
)

stages = {
    "_01_dl_track": _01_dl_track,
    "_02_prepare_track": _02_prepare_track,
    "_03_interp_on_track": _03_interp_on_track,
    "_04_1_lambdax": _04_1_lambdax,
    "_04_2_mu": _04_2_mu,
}


params = dict(
    method="default",
    study_path="data/downloads/method_outputs/${.method}.nc",
    study_var="ssh",
    sat="c2",
    min_time="2017-01-01",
    max_time="2017-12-31",
    min_lon=-65.0,
    max_lon=-55.0,
    min_lat=33.0,
    max_lat=43.0,
)
pipeline, recipe, params = aprl.appareil.register(
    name="dc_ose_2021_alongtrack_metrics", parts=stages, params=params, help_msg=__doc__
)
