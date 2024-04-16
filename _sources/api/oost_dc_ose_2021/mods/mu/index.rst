:py:mod:`oost_dc_ose_2021.mods.mu`
==================================

.. py:module:: oost_dc_ose_2021.mods.mu


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.mu.mu



Attributes
~~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.mu.log
   oost_dc_ose_2021.mods.mu.b


.. py:data:: log

   

.. py:function:: mu(study_paths: str = 'data/prepared/method_output/map_on_track.nc', ref_paths: str = 'data/prepared/ref/default.nc', output_path: str = 'data/metrics/mu.json', preprocess_ref=None, preprocess_study=None)

       Compute the normalized RMSE score $mu$ as:
       $$ mu =  1 - 
   rac{RMS(ref - study)}{RMS(ref)} $$

       Args:
           output_path (str): Path where to write the json with the score value
           preprocess_ref (xr.Dataset -> xr.DataArray): Preprocessing that returns the reference DataArray
           preprocess_study (xr.Dataset -> xr.DataArray): Preprocessing that returns the analysis DataArray
           study_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the analysis dataset
           ref_paths (str | Path | Sequence): path(s) to netcdf file(s) containing the reference dataset
       


.. py:data:: b

   

