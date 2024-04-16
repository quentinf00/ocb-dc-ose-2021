:py:mod:`oost_dc_ose_2021.pipelines.input_data`
===============================================

.. py:module:: oost_dc_ose_2021.pipelines.input_data


Module Contents
---------------

.. py:data:: cmems_get_cfg

   

.. py:data:: dataset_id_cfg

   

.. py:data:: regex_cfg

   

.. py:data:: _01_dl_track

   

.. py:data:: prepare_track_cfg

   

.. py:data:: input_paths_cfg

   

.. py:data:: preprocess_cfg

   

.. py:data:: _02_prepare_track

   

.. py:data:: stages

   

.. py:data:: params

   

.. py:data:: sweep

   

.. py:data:: help_msg
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        Overview:
            Download and prepare data for SSH Mapping (requires CMEMS credentials for download)
            The ssh is computed as "sla_filtered + mdt - lwe"
        
        Basic CLI Usage:
          *  params.sat=<sat_id> to download a prepare a specific satellite
        
          *  --multirun: Execute the pipeline for each sat in sat_list
        
          *  params.(min|max)_(lon|lat|time)=<bound> to change the bound
        
          *  `-cd conf overrides=my_conf` to load config from conf/aprl/overrides/my_conf.yaml
        
        Params:
            sat (str): altimeter id to download (place holder for multirun)
            sat_list (str): list of satellite to download
            min_time: start of the temporal domain
            max_time: end of the temporal domain
            min_lon: lower longitudinal bound
            max_lon: upper longitudinal bound
            min_lat: upper latitudinal bound
            max_lat: upper latitudinal bound
        """

    .. raw:: html

        </details>

   

