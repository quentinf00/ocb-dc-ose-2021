# Leaderboard Datachallenge OSE 2021


We provide here the resources to reproduce all the processing and evaluating steps as well as access to intermediary data productions.

## Fetch the data


The data tree looks like:
```
data
├── downloads           # unprocessed data are not versioned
├── metrics             # light json files are versioned with git
│   ├── lambdax_duacs.json
│   └── mu_duacs.json
└── prepared            # are versioned with dvc
    ├── input
    │   ├── alg.nc
    │   ├── h2ag.nc
    │   ├── j2g.nc
    │   ├── j2n.nc
    │   ├── j3.nc
    │   └── s3a.nc
    ├── methods         # are versioned with dvc
    │   ├── duacs_on_track.nc
    │   └── psd_duacs.nc
    └── ref             # are versioned with dvc
        └── c2.nc
```

Requirements:
dvc

you can fetch the data versioned by dvc with:
`dvc pull`


## Reproduce the data processing and results

```
dvc repro -f -s update_config
dvc repro diagnostics/
```

## Add your method

Requirements:
you should have generated a netcdf with "lat","lon","time" coordinates and made it available by https


Add a section in methods.toml for <yourmethod>

```
[methods.<yourmethod>]
url = "<yourmethodoutputurl>"
var = "ssh" 
```

test it locally with dvc repro


## Leaderboard

```
dvc metrics show --json | python scripts/format_metrics.py
```
