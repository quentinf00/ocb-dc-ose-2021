:py:mod:`oost_dc_ose_2021.mods.lambdax`
=======================================

.. py:module:: oost_dc_ose_2021.mods.lambdax


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.lambdax.min_intersect
   oost_dc_ose_2021.mods.lambdax.lambdax



Attributes
~~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.lambdax.log
   oost_dc_ose_2021.mods.lambdax.b


.. py:data:: log

   

.. py:data:: b

   

.. py:function:: min_intersect(ds, threshold=0.5, dvar='score', dim='wavenumber')

   Find the first (minimum) coordinates at which a variable passes a threshold

   Args:
       ds (xarray.Dataset): 1 netcdf
       threshold (float): threshold
       dvar (str): 1D dataset variable to pass the threshold
       dim (str): dataset dimension on which to select the intersect

   Returns: dim value linearly interpolated at which dvar is threshold



.. py:function:: lambdax(study_paths: str | Sequence[str] = 'data/prepared/method_output/map_on_track.nc', ref_paths: str | Sequence[str] = 'data/prepared/ref/default.nc', delta_t: float = 0.9434, velocity: float = 6.77, length_scale: float = 1000, segment_overlapping: float = 0.25, output_lambdax_path: str = 'data/metrics/lambdax.json', output_psd_path: str = 'data/method_outputs/psd_score.nc', preprocess_ref: Callable[[xarray.Dataset], xarray.DataArray] = b(operator.attrgetter, 'ssh'), preprocess_study: Callable[[xarray.Dataset], xarray.DataArray] = b(operator.attrgetter, 'ssh'))

       Compute the PSD of the reference signal and the error and calulate the first wavelength $lambda_x$ at which
       $$ 1 - 
   rac{PSD_{err}(lambda_x)}{PSD_{ref}(lambda_x)} = 0.5 $$

       Args:
           output_lambdax_path (str): Path where to write the json with the score value
           output_psd_path (str): Path where to write the netcdf with the PSD
           preprocess_ref (xr.Dataset -> xr.DataArray): Preprocessing that returns the reference DataArray
           preprocess_study (xr.Dataset -> xr.DataArray): Preprocessing that returns the analysis DataArray
           study_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the analysis dataset
           ref_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the reference dataset
           delta_t (float): Sampling of the reference altimeter
           velocity (float): Speed of the reference altimeter
           length_scale (float): Segment length
           segment_overlapping (float): overlapping proportion between two segments
       


