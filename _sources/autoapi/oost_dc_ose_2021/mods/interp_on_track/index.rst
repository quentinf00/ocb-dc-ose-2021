:py:mod:`oost_dc_ose_2021.mods.interp_on_track`
===============================================

.. py:module:: oost_dc_ose_2021.mods.interp_on_track


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.interp_on_track.preprocess_map
   oost_dc_ose_2021.mods.interp_on_track.interp_on_track



Attributes
~~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.interp_on_track.log
   oost_dc_ose_2021.mods.interp_on_track.b
   oost_dc_ose_2021.mods.interp_on_track.pb


.. py:data:: log

   

.. py:function:: preprocess_map(ds, ssh_var='ssh')

   Check presence of time, lat, lon coordinates
   Set units to longitude, latitude, ssh variable
   Set range of longitude between -180 and 180
   Select ssh variable

   Args:
       ds (xarray.Dataset): input dataset
       ssh_var (str): Sea surface height variable

   Returns: validated xarray.Dataset


.. py:function:: interp_on_track(grid_paths, track_paths, output_path, preprocess_grid=None, preprocess_track=None)

   Sample a map along an altimeter track

   The input data is read using:
   ```
       xr.open_mfdataset(
           paths, preprocess=preprocess, combine="nested", concat_dim="time"
       )
   ```

   Args:
       grid_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the data to sample
       track_paths (str | Path | Sequence): path(s) to netcdf file(s) containing alongtrack data with a time dimension
       output_path (str): path where to write the output
       preprocess_grid (callable): function to apply to each grid netcdf
       preprocess_track (callable): function to apply to each grid netcdf


.. py:data:: b

   

.. py:data:: pb

   

