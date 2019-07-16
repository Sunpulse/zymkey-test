#!/bin/bash
set -e

# set current working directory to the directory of this script
cd "$(dirname ${BASH_SOURCE[0]})"

VENV_HOME=./venv

$VENV_HOME/bin/python -u src/start-with-timeout.py
