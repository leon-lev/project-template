.PHONY: venv test clean

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PACKAGE_NAME = {{cookiecutter.package_name}}
SHELL := /usr/bin/bash # set bash as global shell

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## install dependencies using pip
venv: requirements.txt
	(\
	python3 -m venv venv_{{cookiecutter.package_name}};\
	source venv_{{cookiecutter.package_name}}/bin/activate;\
	pip3 install -e .;\
	)


test:
	pytest


clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete