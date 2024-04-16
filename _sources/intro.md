# Ocean Observation Science Toolkit: SSH Data challenge Design


## Overall presentation

### Related projects
This project can be seen as an iteration over existing work.

Firstly **[ocean-data-challenges](https://ocean-data-challenges.github.io/)** which propose framed ocean observation tasks with input data and relevant metrics. Those data challenges provide a great catalyzer for academic collaboration on shared issues by facilitating the inter-comparison of methods.
Then **[oceanbench](https://jejjohnson.github.io/oceanbench/content/overview.html)** aimed at lowering the barrier of entry to ocean science by proposing utility tools for ocean data processing ([ocn-tools](https://github.com/jejjohnson/ocn-tools/), data access ([data-registry](https://github.com/quentinf00/oceanbench-data-registry)), domain patching and stitching ([xrpatcher](https://github.com/jejjohnson/xrpatcher)) and  an configuration registry to showcase the orchestration of those different tools [oceanbench](https://github.com/jejjohnson/oceanbench)

Building on those project, we aim at laying the foundations for a collaborative and evolutive ecosystem that facilitate:
- Sharing experimental setups, data, methods, metrics and processing steps
- Reproducing data processing and results 
- Extending and evolving experimental setups, data processing, methods

This book presents the repo `https://github.com/quentinf00/oost-demo-ssh-dc.git` which is an re-implementation of the [2021a_SSH_mapping_OSE data-challenge](https://github.com/ocean-data-challenges/2023a_SSH_mapping_OSE) aiming at showcasing this attempt

## New concepts, Tools and Features:

### Data challenge features:
This implementation offers the following improvement over the previous implementation:
- Data access made easier (single command to download the prepared data)
- Reproducibility and constistence (of metrics and data prep)
- Automatic leaderboard computation (when adding or updating a method or updating the metrics)
- Resusability of processing steps (data, metrics) for other use-cases made easy

### Concepts:
Those new features are made possible through the use of the following concepts:
- **Versioned data**: being able to store, access and compare different version of a dataset
- **Workflow management**: orchestrating the tasks involved in processing the data and generating the results
- **Continuous integration**: Automatically running tasks when changes are made
- **Application packaging**: Providing portable and customizable interfaces to the software

### Tools
In order to implement the previous concepts, the following tools and library
-  **[hydra](https://hydra.cc/docs/intro/) and [hydra-zen](https://mit-ll-responsible-ai.github.io/hydra-zen/)** provide:
    -  python <-> configuration workflow (share code, adapt config) 
    -  CLI integration
    -  easy // computing (local, cluster), logging 
-  **[dvc](https://dvc.org/doc/use-cases)** provides:
    -  data versioning via git indexed cloud storage
    -  workflow management 
- **[github actions](https://docs.github.com/en/actions)**
    - continuous integration
  


## Feature Showcase
We provide through the following notebooks and associated 5 min walkthrough videos demonstrations on the new features brought by this implementations
![](imgs/contrib_doc.png)
- Versioned data access and reproduction for data challenges
<iframe width="560" height="315" src="https://www.youtube.com/embed/9sMfMNRIaJA?si=2r3As5ZdwhrWZkPk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- Metrics computation and automated leaderboard update
- Reusing the pipelines for a global usecase



```{tableofcontents}
```
