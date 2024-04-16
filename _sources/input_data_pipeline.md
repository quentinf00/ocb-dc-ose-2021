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


# `oost-dc_ose_2021-input_data`


```{code-cell} ipython3
---
tags:
    - hide-cell
---
from myst_nb import glue
from IPython.display import Markdown
import oost_dc_ose_2021.pipelines.input_data as inp_pipe
glue('inp_data_doc', Markdown(inp_pipe.__doc__), display=False)

import hydra_zen
params = Markdown('`'*3 +'yaml\n'+
hydra_zen.to_yaml(inp_pipe.params)+
'\n' + '`'*3)
glue('inp_data_params', params, display=False)

import hydra

stages = inp_pipe.stages
stage_md = "" 
for k, cfg in stages.items():
    stage_md += f'### {k}:\n'
    stage_md += f'#### Documentation:\n'
    stage_md += hydra.utils.get_object(cfg._target_).__doc__ + '\n'
    stage_md += f'#### Configuration:\n'
    stage_md += ('`'*3 +'yaml\n'+
        hydra_zen.to_yaml(cfg)+
        '\n' + '`'*3 + '\n'
    )
glue('inp_data_stages', Markdown(stage_md), display=False)
```

``` {glue:md} inp_data_doc
:format: myst
```

## Default params:
``` {glue:md} inp_data_params
:format: myst
```

## Stages:
``` {glue:md} inp_data_stages
:format: myst
```
