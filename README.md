# autoengage
Master repo with autoengage.

[![CircleCI](https://circleci.com/gh/aamplifyus/autoengage.svg?style=svg&circle-token=be3280d393039eac5067ac529b59241a235a2d4d)](https://circleci.com/gh/aamplifyus/autoengage)
[![Coverage Status](./coverage.svg)](./coverage.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Performs auto-engagement for social media bots and email services.

# Installation Guide
autoengage is intended to be a lightweight wrapper for easily analyzing large batches of patients with EEG data. eegio relies on the following libraries to work:

    numpy
    scipy
    scikit-learn
    pandas
    joblib
    requests
    requests-html 
    bs4
     colorama
      stem 
      selenium
    openpyxl
    matplotlib
    seaborn
    
Setup environment from source

    make inplace

Setup environment directly via recipe:

    conda env create -f ./environment.yml --name=autoengage
        
To install CLI:
    
    conda install click
    make install-cli
     
## Install from Github
To install, run this command in your repo:

    git clone https://github.com/aamplifyus/autoengage
    python setup.py install

or 

    pip install https://api.github.com/repos/aamplifyus/autoengage/zipball/master

# Documentation

    conda install sphinx sphinx-gallery sphinx_bootstrap_theme numpydoc 
    sphinx-quickstart
    make build_doc
    
# Setup Jupyter Kernel To Test
You need to install ipykernel to expose your conda environment to jupyter notebooks.
   
    conda install ipykernel
    python -m ipykernel install --name autoengage --user
    # now you can run jupyter lab and select a kernel
    jupyter lab 

# Testing
Install testing and formatting libs:

    conda install black pytest pytest-cov coverage codespell pydocstyle
    pip install coverage-badge anybadge
    
Run tests

    black autoengage/*
    black tests/*
    pylint ./autoengage/
    anybadge --value=6.0 --file=pylint.svg pylint
    pytest --cov-config=.coveragerc --cov=./autoengage/ tests/
    pytest --cov-config=.coveragerc --cov=./autoengage/ tests/ > docs/tests/test_docs.txt
    coverage-badge -f -o coverage.svg
    