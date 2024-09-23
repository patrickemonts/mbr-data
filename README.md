# Data for multiple basis representation manuscript

This repsoitory contains the data to generate the plots in the manuscript "XXX" (arXiv:2409.XXXXX).

## Table of Contents

- [Data for topological Bell manuscript](#data-for-topological-bell-manuscript)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction

Each script in the main folder produces one plot of the paper (arxiv:2405.XXXX).
The scripts do *not* take command line parameters and the data sources are hard-coded on purpose.
This repository is not a development directory, but a data archive.

## Installation

The code is written for Python 3 and tested to work with Python 3.8.

To make sure that all requirements of the package are fulfilled, the easiest way to use the code is to create a virtual environment and install the necessary packages independent of the python packages of the operating system

1. Creation of a virtual environment  
You can create the environment in a folder of your choice. 
For the rest of the tutorial, we assume it to be in `~/.pyenv/`
```
cd ~/.pyenv
python -m venv mbrenv
```
Assuming you are using bash or zsh, you can activate the environment with `source ~/.pyenv/mbrenv/bin/activate`.
Upon activation, you will notice that your prompt changes.
As long as it is prefixed with `(mbrenv)` the virtual environment is active.
The virtual environment can be deactivated with `deactivate`.

2. Cloning the code  
You can obtain the code by cloning the repo with
```
git clone git@gitlab.com:XXXX
```

3. Preparation of the environment  
For the next step, please navigate into the repo that you just downloaded and activate the empty environment that we created in step 1.
In order to install all required packages for the simulation, execute
```
pip install -r requirements.txt
```

4. Modification of the PYTHONPATH  
Since we are working with a package (`mbrenv`), we have to add it to the PYTHONPATH in order to make Python aware of its existence.
We add the repository to the PYTHONPATH with the following command
```export PYTHONPATH=$PYTHONPATH:<path_to_repo>```
where `<path_to_repo>` is the location of the repository on your computer.

If you want to make the change persistent, i.e. it remains after closing the terminal, you can consider adding it to your `~/.bashrc` (for bash) or `~/.zshrc` (for zsh).

At a later stage a proper installation via a `setup.py` script will be added.

## Usage

After loading the environment created in the installation steps, you can generate the plots with
```
python <name_of_script.py>
```
