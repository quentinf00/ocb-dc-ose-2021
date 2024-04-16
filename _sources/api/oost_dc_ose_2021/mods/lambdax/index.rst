:py:mod:`oost_dc_ose_2021.mods.lambdax`
=======================================

.. py:module:: oost_dc_ose_2021.mods.lambdax


Module Contents
---------------

.. py:function:: min_intersect(ds, threshold=0.5, dvar='score', dim='wavenumber')

   Find the first (minimum) coordinates at which a variable passes a threshold

   :param ds: 1 netcdf
   :type ds: xarray.Dataset
   :param threshold: threshold
   :type threshold: float
   :param dvar: 1D dataset variable to pass the threshold
   :type dvar: str
   :param dim: dataset dimension on which to select the intersect
   :type dim: str

   Returns: dim value linearly interpolated at which dvar is threshold



.. py:function:: lambdax(study_paths: str | Sequence[str] = 'data/prepared/method_output/map_on_track.nc', ref_paths: str | Sequence[str] = 'data/prepared/ref/default.nc', delta_t: float = 0.9434, velocity: float = 6.77, length_scale: float = 1000, segment_overlapping: float = 0.25, output_lambdax_path: str = 'data/metrics/lambdax.json', output_psd_path: str = 'data/method_outputs/psd_score.nc', preprocess_ref: Callable[[xarray.Dataset], xarray.DataArray] = _b(operator.attrgetter, 'ssh'), preprocess_study: Callable[[xarray.Dataset], xarray.DataArray] = _b(operator.attrgetter, 'ssh'))

   Compute the PSD of the reference signal and the error and calulate the first wavelength :math:`\lambda_x` at which

   .. math::
       1 - \frac{PSD_{err}(lambda_x)}{PSD_{ref}(\lambda_x)} = 0.5


   :param output_lambdax_path: Path where to write the json with the score value
   :type output_lambdax_path: str
   :param output_psd_path: Path where to write the netcdf with the PSD
   :type output_psd_path: str
   :param preprocess_ref: Preprocessing that returns the reference DataArray
   :type preprocess_ref: xr.Dataset -> xr.DataArray
   :param preprocess_study: Preprocessing that returns the analysis DataArray
   :type preprocess_study: xr.Dataset -> xr.DataArray
   :param study_paths: path(s) to netcdf file(s) containing the analysis dataset
   :type study_paths: str | Path | Sequence
   :param ref_paths: path(s) to netcdf file(s) containing the reference dataset
   :type ref_paths: str | Path | Sequence
   :param delta_t: Sampling of the reference altimeter
   :type delta_t: float
   :param velocity: Speed of the reference altimeter
   :type velocity: float
   :param length_scale: Segment length
   :type length_scale: float
   :param segment_overlapping: overlapping proportion between two segments
   :type segment_overlapping: float


