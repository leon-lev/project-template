import os

from setuptools import find_packages, setup

# avoid installing external dependencies when conda is used
# (conda will take care of that)
use_conda = os.environ.get('USE_CONDA')
if use_conda=='true':
    requirements = []
else:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

setup(
    name='{{cookiecutter.package_name}}',
    packages=find_packages(exclude=("tests",)),
    install_requires=requirements,
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='MIT',
)