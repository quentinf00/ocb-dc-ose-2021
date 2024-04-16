:py:mod:`oost_dc_ose_2021.mods.prepare_track`
=============================================

.. py:module:: oost_dc_ose_2021.mods.prepare_track


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.prepare_track.preprocess_track
   oost_dc_ose_2021.mods.prepare_track.prepare_track



Attributes
~~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.prepare_track.log
   oost_dc_ose_2021.mods.prepare_track.b
   oost_dc_ose_2021.mods.prepare_track.pb


.. py:data:: log

   

.. py:function:: preprocess_track(ds: xarray.Dataset, min_lon: float = -66, max_lon: float = -54, min_lat: float = 32, max_lat: float = 44, min_time: str = '2016-12-01', max_time: str = '2018-02-01')

   Check presence of time, lat, lon coordinates
   Set units to longitude, latitude, ssh variable
   Set range of longitude between -180 and 180
   Selecting SSH variable
   Filter values between min_max values for lat, lon and time

   Args:
       ds: Dataset
       min_lon: min longitude value
       max_lon: max longitude value
       min_lat: min latitude value
       max_lat: max latitude value
       min_time: min time value
       max_time: max time value

   Returns: xarray.Dataset



.. py:function:: prepare_track(input_paths: str | Sequence[str], output_path: str, preprocess: Callable[[xarray.Dataset], xarray.Dataset], sort_paths: bool = True)

   Open multifile dataset to be contatenated by time apply processing and write output

   Args:
       input_paths (str | Path | Sequence): path(s) to input netcdf file(s)
       output_path (str): path where to write the output
       preprocess (callable): function to apply to each netcdf
       sort_paths (bool): whether to sort input_paths before concatenation


.. py:data:: b

   

.. py:data:: pb

   

