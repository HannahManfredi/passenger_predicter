#!/bin/bash

set -e

pipenv --python 3.11
pipenv install ipykernel==6.28.0 python-dotenv==1.0.0
pipenv run python -m ipykernel install --user --name="passenger_predictor" --display-name="passenger_predictor"
pipenv install