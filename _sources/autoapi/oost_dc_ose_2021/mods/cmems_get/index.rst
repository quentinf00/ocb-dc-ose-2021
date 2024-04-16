:py:mod:`oost_dc_ose_2021.mods.cmems_get`
=========================================

.. py:module:: oost_dc_ose_2021.mods.cmems_get


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.cmems_get.month_regex_from_date
   oost_dc_ose_2021.mods.cmems_get.duacs_l3



Attributes
~~~~~~~~~~

.. autoapisummary::

   oost_dc_ose_2021.mods.cmems_get.b


.. py:function:: month_regex_from_date(min_time: str = '2017-01-01', max_time: str = '2017-12-31')

   Constructs a regex matching any month %Y%m from time period

   Args:
       min_time (str): start of the period
       max_time (str): end of the period

   Returns: Regex string



.. py:function:: duacs_l3(sat: str = 'c2')

   Construct from altimeter id the cmems dataset_id for DUACS L3 reprocessed altimetry tracks:
       "cmems_obs-sl_glo_phy-ssh_my_{sat}-l3-duacs_PT1S"
   Args:
       sat (str): altimeter id

   Returns: dataset_id


.. py:data:: b

   

