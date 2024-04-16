:py:mod:`oost_dc_ose_2021.mods.cmems_get`
=========================================

.. py:module:: oost_dc_ose_2021.mods.cmems_get


Module Contents
---------------

.. py:function:: month_regex_from_date(min_time: str = '2017-01-01', max_time: str = '2017-12-31')

   Constructs a regex matching any month %Y%m from time period

   :param min_time: start of the period
   :type min_time: str
   :param max_time: end of the period
   :type max_time: str

   Returns: Regex string



.. py:function:: duacs_l3(sat: str = 'c2')

   Construct from altimeter id the cmems dataset_id for DUACS L3 reprocessed altimetry tracks:
       "cmems_obs-sl_glo_phy-ssh_my_{sat}-l3-duacs_PT1S"
   :param sat: altimeter id
   :type sat: str

   Returns: dataset_id


