# Setup



## Installing the conda environment

Prerequisites:

- `mamba` (or `conda`)
- `conda-merge` (pip install conda-merge)
- `ipython`, `jupyter`

The installation requires conda.
Depending on you usage you may not need a full install.
The dependencies have therefore been splitted in different files in the envs folder of the repository https://github.com/quentinf00/oost-dc-ose-2021.git.
The installation relies on conda-merge to compile multiple file into one environment file suited to your need.
Below an example of a full install to reproduce the demo

### Without cloning
```
wget -nc https://raw.githubusercontent.com/quentinf00/oost-dc-ose-2021/envs/{docs,base,dc,dvc-s3}.yaml
conda merge {docs,base,dc,dvc-s3}.yaml > env.yaml
mamba env create --quiet -n oost-docs -f env.yaml
```

### With cloning
```
git clone https://github.com/quentinf00/oost-dc-ose-2021.git
conda merge oost-dc-ose-2021/envs/{docs,base,dc,dvc-s3}.yaml > env.yaml
mamba env create --quiet -n oost-docs -f env.yaml
```

### On colab
In the first cell run:
```
!pip install -q condacolab conda-merge
import condacolab
condacolab.install_mambaforge()
```


## Credentials needed to reproduce the demo notebooks

### CMEMS: to fetch source data from the copernicus portal
If you don't have credentials: go [here](https://data.marine.copernicus.eu/register)

to login using the CLI
```bash
copernicusmarine login # installed with base dependencies
```

### AWS: to push prepared data to cloud storage or upload method result for leaderboard submission
you can authentificate using:

```bash
aws configure
```

or setting the environment variables: `AWS_ENDPOINT_URL` `AWS_DEFAULT_REGION` `AWS_SECRET_ACCESS_KEY` `AWS_ACCESS_KEY_ID`

### GITHUB: to create a `leaderboard` pull request on the repo (from the original or a fork)

