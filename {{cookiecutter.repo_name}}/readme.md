# {{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}


## Environment Setup

Instructions for the installation of the package into a virtual environment are specified below.
You can use either conda or pip + venv.

1. Using pip + venv:

    Simply type `make venv` (if make is installed). 
    
    Alternatively use the following commands:
    ```
	python3 -m venv venv_{{cookiecutter.package_name}}
	source venv_{{cookiecutter.package_name}}/bin/activate
	pip3 install -e .
    ```
 
2. Using [conda](https://www.anaconda.com/):

    ```
    conda env create --name {{cookiecutter.package_name}} --file environment.yml
    conda activate {{cookiecutter.package_name}}
	export USE_CONDA=true
    pip3 install -e .
	unset USE_CONDA
    ```
    The flag `USE_CONDA` is used to prevent pip from installing redundant packages over conda.