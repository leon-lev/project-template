# Data-Science Project Template

This template is based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/) and the [cookiecutter Pytorch template](https://github.com/khornlund/cookiecutter-pytorch). #cookiecutterdatascience.

## Project Organization
------------

    ├── package_name       <- Source code for use in this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── resources          <- Miscellaneous explanatory materials.
    │
    ├── experiments        <- Generated figures, summaries, reports etc.
    │
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── environment.yml    <- Conda environment file, generated with
    ├──                       `conda env export --no-builds | grep -v "prefix" > environment.yml`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │   ├── __init__.py    <- Makes the folder a Python module
    │   │
    │   ├── data           <- Scripts to download, generate and transform data
    │   │
    │   ├── model          <- Scripts to train, apply (predict) and evaluate models
    │   │   └── model.py
    │   │
    │   └── utils          <- Scripts of various utitlities (explorations, visualizations etc.)
    │       └── utils.py
    │
    └── tests              <- Scripts for tests


--------
