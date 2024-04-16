:py:mod:`oost_dc_ose_2021.mods.prepare_track`
=============================================

.. py:module:: oost_dc_ose_2021.mods.prepare_track


Module Contents
---------------

.. py:function:: preprocess_track(ds: xarray.Dataset, min_lon: float = -66, max_lon: float = -54, min_lat: float = 32, max_lat: float = 44, min_time: str = '2016-12-01', max_time: str = '2018-02-01')

   Check presence of time, lat, lon coordinates
   Set units to longitude, latitude, ssh variable
   Set range of longitude between -180 and 180
   Selecting SSH variable
   Filter values between min_max values for lat, lon and time

   :param ds: Dataset
   :param min_lon: min longitude value
   :param max_lon: max longitude value
   :param min_lat: min latitude value
   :param max_lat: max latitude value
   :param min_time: min time value
   :param max_time: max time value

   Returns: xarray.Dataset



.. py:function:: prepare_track(input_paths: str | Sequence[str], output_path: str, preprocess: Callable[[xarray.Dataset], xarray.Dataset], sort_paths: bool = True)

   Open multifile dataset to be contatenated by time apply processing and write output

   :param input_paths: path(s) to input netcdf file(s)
   :type input_paths: str | Path | Sequence
   :param output_path: path where to write the output
   :type output_path: str
   :param preprocess: function to apply to each netcdf
   :type preprocess: callable
   :param sort_paths: whether to sort input_paths before concatenation
   :type sort_paths: bool


