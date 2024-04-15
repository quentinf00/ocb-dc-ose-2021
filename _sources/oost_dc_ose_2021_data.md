---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: oost-docs
  language: python
  name: oost-docs
---

# Versioned data download and reproduction


## Reusing processing steps and reproducing data preparation

### Use the configured `oost-dc_ose_2021-input_data` pipeline
![data schema](imgs/data_doc.png)

#### Reproduce processing of single satellite

```{code-cell} ipython3
!oost-dc_ose_2021-input_data --cfg job -p params
```

```{code-cell} ipython3
:tags: [scroll-output]

!oost-dc_ose_2021-input_data params.sat=j2g
```

```{code-cell} ipython3
import xarray as xr
ds = xr.open_mfdataset('data/prepared/input/*.nc', combine='nested',concat_dim='time')
ds
```

```{code-cell} ipython3
# 2D map
bin_size = 1/20
(
    ds.sel(time='2017-08-01').assign(
        lat=ds.lat / bin_size // 1 * bin_size,
        lon=ds.lon / bin_size // 1 * bin_size
    )[['ssh', 'lat', 'lon']].load()
    .drop_vars('time')
    .to_dataframe()
    .groupby(['lat', 'lon']).mean()
    .to_xarray()
).ssh.plot()
```

#### Dry (without actual execution) run for all satellites

```{code-cell} ipython3
!oost-dc_ose_2021-input_data --multirun dry=True
```

## Downloading versioned and preprocessed data

![dvc schema](imgs/dvc_doc.png)
### Listing datachallenge content

```{code-cell} ipython3
# Storing the repo url for convenience
%env DC_REPO=https://github.com/quentinf00/oost-demo-ssh-dc.git
```

```{code-cell} ipython3
# Listing and pretty printing all files of the datachallenge
!dvc ls -R $DC_REPO datachallenge/data | tree --fromfile
```

### Downloading prepared input data

```{code-cell} ipython3
!dvc get -q $DC_REPO datachallenge/data/prepared/input
```

```{code-cell} ipython3
!tree input
```

### Visualize input data

```{code-cell} ipython3
ds = xr.open_mfdataset('input/*.nc', combine='nested',concat_dim='time')
ds
```

```{code-cell} ipython3
# 2D map
bin_size = 1/20
(
    ds.sel(time='2017-08-01').assign(
        lat=ds.lat / bin_size // 1 * bin_size,
        lon=ds.lon / bin_size // 1 * bin_size
    )[['ssh', 'lat', 'lon']].load()
    .drop_vars('time')
    .to_dataframe()
    .groupby(['lat', 'lon']).mean()
    .to_xarray()
).ssh.plot()
```

### Checking generated data VS downloaded

```{code-cell} ipython3
xr.testing.assert_allclose(
    xr.open_dataset('data/prepared/input/j2g.nc'),
    xr.open_dataset('input/j2g.nc'),
)
print("Successful reproduction")
```

### More on pipeline usage (help, doc, ...)

```{code-cell} ipython3
!oost-dc_ose_2021-input_data --help
```

```{code-cell} ipython3
!oost-dc_ose_2021-input_data params.sat=alg dry=True 'hydra.verbose=[aprl.appareil]'
```
