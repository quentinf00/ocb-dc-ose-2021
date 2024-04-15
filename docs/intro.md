# Ocean Observation Science Toolkit: SSH Data challenge Design


## Overall presentation
This book presents the repo `https://github.com/quentinf00/oost-demo-ssh-dc.git` which is an re-implementation of the [2021a_SSH_mapping_OSE data-challenge](https://github.com/ocean-data-challenges/2023a_SSH_mapping_OSE).
 This project introduces a series of tools and practices that aims at facilitating the development and application of ocean observation science.

## New concepts, Tools and Features:


### Features:
- Data access made easier
- Guaranteed reproducibility
- Automatic leaderboard computation
- Easy extensibility of data  and metric computations to other use-cases

### Concepts:
- **Versioned data**: being able to store, access and compare different version of a dataset
- **Workflow management**: orchestrating the tasks involved in processing the data and generating the results
- **Continuous integration**: Automatically running tasks when changes are made
- **App packaging**: Providing reusable and customizable interfaces to the software

  
### Tools
-  **[hydra](https://hydra.cc/docs/intro/) and [hydra-zen](https://mit-ll-responsible-ai.github.io/hydra-zen/)** provide:
    -  python <-> configuration workflow (share code, adapt config) 
    -  CLI integration
    -  easy // computing (local, cluster), logging 
-  **[dvc](https://dvc.org/doc/use-cases)** provides:
    -  data versioning via git indexed cloud storage
    -  workflow management 
- **[github action](https://docs.github.com/en/actions)**
    - continuous integration
  

### related projects
- **[ocean-data-challenges](https://ocean-data-challenges.github.io/)** provide:
    - well thought evaluation use cases
    - input data download instructions
    - metrics code and notebooks to evaluate methods
-  **[oceanbench](https://jejjohnson.github.io/oceanbench/content/overview.html)** provide:
    -  suite of tools and configuration for developing ml application


## Feature Showcase
We provide through the following notebooks and associated 5 min walkthrough videos demonstrations on the new features brought by this implementations
![](imgs/contrib_doc.png)
- Versioned data access and reproduction for data challenges
<iframe width="560" height="315" src="https://www.youtube.com/embed/9sMfMNRIaJA?si=2r3As5ZdwhrWZkPk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- Metrics computation and automated leaderboard update
- Reusing the pipelines for a global usecase



```{tableofcontents}
```
