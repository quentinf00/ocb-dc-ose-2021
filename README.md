# Oceanbench data challenge demo

## Installation:
### Usage: Download prepared input data
```
git 
```

## Modules:

- cmems_get: download data from cmems portal
- prepare_track: filter, merge, compute SSH as sla_filtered + mdt -lwe
- interp_on_track: sample a map on the track geometry
- lambdax: compute effective spatial scale in the track geometry
- mu: compute normalized rmse score

## Pipelines:
- input_data: `ocb-dc_ose_2021-input_data`
- metrics: `ocb-dc_ose_2021-metrics`





