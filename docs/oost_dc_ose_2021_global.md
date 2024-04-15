---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: oost
  name: oost-docs
---

# Reusing the pipelines for a global usecase

## Creating novel input data configuration

### Visualizing the fields and their explanations
```{code-cell}
!oost-dc_ose_2021-input_data --cfg job -p params
```

```{code-cell}
---
tags:
  - scroll-output
---
!oost-dc_ose_2021-input_data --help
```

### Writing new file



```{code-cell}
!mkdir -p conf/aprl/overrides
```

```{code-cell}
%%writefile conf/aprl/overrides/global.yaml
# @package params

sat_list: [j3, s3b, h2ag, c2]
min_time: 2019-05-01
max_time: 2019-05-31
min_lon: -180
max_lon: 180
min_lat: -90
max_lat: 90
```

```{code-cell}
---
tags:
  - scroll-output
---
%%bash
oost-dc_ose_2021-input_data -m \
    'hydra.searchpath=[file://conf]'  +overrides@params=global\
     dry=True
```

```{code-cell}
---
tags:
  - scroll-output
---
%%bash
oost-dc_ose_2021-input_data -m \
    'hydra.searchpath=[file://conf]' \
      +overrides@params=global \
      hydra/launcher=joblib \
      hydra.launcher.n_jobs=4 
```

```{code-cell}
import xarray as xr
import pandas as pd

obs = xr.open_mfdataset('data/prepared/input/*.nc', combine='nested',concat_dim='time')
obs
```

```{code-cell}
---
tags:
  - hide-input
---
import hvplot.xarray
import hvplot
hvplot.extension('matplotlib')
%matplotlib inline

bin_size = 0.25
to_plot = (obs.where((obs.time>pd.to_datetime('2019-05-15')) & (obs.time<pd.to_datetime('2019-05-16')) )
.drop_vars('time').assign(
        lat=obs.lat / bin_size // 1 * bin_size,
        lon=obs.lon / bin_size // 1 * bin_size
    )[['ssh', 'lat', 'lon']].load()
    .drop_vars('time')
    .to_dataframe()
    .groupby(['lat', 'lon']).mean()
    .to_xarray()
).ssh
hvfig = to_plot.hvplot(
    kind='quadmesh',
    geo=True,
    coastline=True,
    width=1000,
    cmap='RdYlBu_r'
)
bokfig = hvplot.render(hvfig, backend='matplotlib')
bokfig
```

```{code-cell}
---
tags:
  - hide-cell
---
!wget https://gist.githubusercontent.com/quentinf00/2d034392ee9b385fb4de3c8628bfc844/raw/aaeaed8ce5a1559507be8dd52e37c134f777192c/patcher_oi_torch.py
```

<script src="https://gist.github.com/quentinf00/2d034392ee9b385fb4de3c8628bfc844.js"></script>

```{code-cell}
---
tags:
  - scroll-output
---
import numpy as np
import xarray as xr
import pandas as pd
from functools import partial
from xrpatcher import XRDAPatcher
from patcher_oi_torch import oi


outgrid = oi(
    outgrid_da=xr.DataArray(
        dims=('time', 'lat', 'lon'),
        coords=dict(
            time=pd.date_range('2019-05-15', '2019-05-15'),
            lat=np.arange(-90, 90, .25),
            lon=np.arange(-180, 180, .25),
        ),
    ),
    patcher_cls=partial(XRDAPatcher,
        patches=dict(time=1, lat=80, lon=80),
        strides=dict(time=1, lat=80, lon=80)
    ),
    obs=obs.load(),
    lt=pd.to_timedelta('7D'), lx=1., ly=1.,
    noise=0.05,
    obs_dt=pd.to_timedelta('2D'), obs_dx=.5, obs_dy=.5,
    device='cuda'
)
```

```{code-cell}
---
tags:
  - hide-input
---
from global_land_mask import globe
lat = outgrid.lat.values
lon = outgrid.lon.values
lon_grid, lat_grid = np.meshgrid(lon,lat)
globe_ocean_mask = globe.is_ocean(lat_grid, lon_grid)
out_plot = (
    outgrid.sel(time='2019-05-15').where(globe_ocean_mask)
    .pipe(lambda ds: ds.where(ds <3))
    .pipe(lambda ds: ds.where(ds >-3))
)
hvfig = out_plot.hvplot(
    kind='quadmesh',
    geo=True,
    coastline=True,
    width=1000,
    cmap='RdYlBu_r'
)
bokfig = hvplot.render(hvfig, backend='matplotlib')
bokfig
```

```{code-cell}
---
tags:
  - hide-input
---
import ocn_tools._src.geoprocessing.geostrophic as geo
import ocn_tools._src.geoprocessing.validation as val
hvfig = (
    out_plot
    .where(np.abs(out_plot.lat)>10)
    .to_dataset(name='ssh')
    .pipe(val.validate_latlon)
    .pipe(geo.geostrophic_velocities)
    .pipe(geo.kinetic_energy)
).ke.hvplot(
    kind='quadmesh',
    geo=True,
    width=1000,
    cmap='viridis',
    clim=(0, 0.3)
)
bokfig = hvplot.render(hvfig, backend='matplotlib')
bokfig
```

```{code-cell}
!oost-dc_ose_2021-metrics --cfg job -p params
```

```{code-cell}
%%writefile conf/aprl/overrides/global_eval.yaml
# @package params

study_path: output.nc
study_var: ssh
sat: alg
min_time: '2019-05-15'
max_time: '2019-05-16'
min_lon: -180
max_lon: 180
min_lat: -90
max_lat: 90
```

```{code-cell}
---
tags:
  - scroll-output
---
%%bash
oost-dc_ose_2021-metrics -m \
    'hydra.searchpath=[file://conf]' \
      +overrides@params=global_eval \
      dry=True
```

```{code-cell}
dt, t = pd.to_timedelta("1D"), pd.to_datetime('2019-05-15')
out_grid = outgrid.pipe(val.validate_latlon).pad(time=1, mode='edge').assign_coords(
    time=pd.date_range(t-dt, t+dt, freq=dt)
).to_dataset(name='ssh')
out_grid.to_netcdf('output.nc')
```

```{code-cell}
---
tags:
  - scroll-output
---
%%bash
oost-dc_ose_2021-metrics \
  'hydra.searchpath=[file://conf]' \
    +overrides@params=global_eval dry=True
```

```{code-cell}
---
tags:
  - scroll-output
---
%%bash
oost-dc_ose_2021-metrics\
    'hydra.searchpath=[file://conf]' \
     +overrides@params=global_eval
```

```{code-cell}
import pandas as pd
import glob
print(pd.concat([pd.read_json(p, typ='series') for p in glob.glob('data/metrics/*.json')]).to_markdown())
```

