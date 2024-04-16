:py:mod:`oost_dc_ose_2021.mods.interp_on_track`
===============================================

.. py:module:: oost_dc_ose_2021.mods.interp_on_track


Module Contents
---------------

.. py:function:: preprocess_map(ds, ssh_var='ssh')

   Check presence of time, lat, lon coordinates
   Set units to longitude, latitude, ssh variable
   Set range of longitude between -180 and 180
   Select ssh variable

   :param ds: input dataset
   :type ds: xarray.Dataset
   :param ssh_var: Sea surface height variable
   :type ssh_var: str

   Returns: validated xarray.Dataset


.. py:function:: interp_on_track(grid_paths, track_paths, output_path, preprocess_grid=None, preprocess_track=None)

   Sample a map along an altimeter track

   The input data is read using:
       xr.open_mfdataset(
           paths, preprocess=preprocess, combine="nested", concat_dim="time"
       )

   :param grid_paths: path(s) to netcdf file(s) containing the data to sample
   :type grid_paths: str | Path | Sequence
   :param track_paths: path(s) to netcdf file(s) containing alongtrack data with a time dimension
   :type track_paths: str | Path | Sequence
   :param output_path: path where to write the output
   :type output_path: str
   :param preprocess_grid: function to apply to each grid netcdf
   :type preprocess_grid: callable
   :param preprocess_track: function to apply to each grid netcdf
   :type preprocess_track: callable


