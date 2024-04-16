:py:mod:`oost_dc_ose_2021.mods.mu`
==================================

.. py:module:: oost_dc_ose_2021.mods.mu


Module Contents
---------------

.. py:function:: mu(study_paths: str = 'data/prepared/method_output/map_on_track.nc', ref_paths: str = 'data/prepared/ref/default.nc', output_path: str = 'data/metrics/mu.json', preprocess_ref=None, preprocess_study=None)

   Compute the normalized RMSE score:

   .. math::
       \mu =  1 - \frac{RMS(ref - study)}{RMS(ref)}

   :param output_path: Path where to write the json with the score value
   :type output_path: str
   :param preprocess_ref: Preprocessing that returns the reference DataArray
   :type preprocess_ref: xr.Dataset -> xr.DataArray
   :param preprocess_study: Preprocessing that returns the analysis DataArray
   :type preprocess_study: xr.Dataset -> xr.DataArray
   :param study_paths: path(s) to netcdf file(s) containing the analysis dataset
   :type study_paths: str | Path | Sequence
   :param ref_paths: path(s) to netcdf file(s) containing the reference dataset
   :type ref_paths: str | Path | Sequence


