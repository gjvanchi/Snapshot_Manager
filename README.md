## Snapshot_Manager

## About
Project to manage AWS EC2 instance snapshots

## Configure
aws configure --profile toronto

##Provide AWS Access Key ID and AWS Secret Access Key

## Requirements
pip3 install pipenv
pipenv --three
pipenv install boto3

#Use ipython to run in command line
#pipenv install -d ipython
#pipenv run ipython

## write code in toronto.py

## Run
pipenv run python toronto/toronto.py
pipenv run python toronto/toronto.py <command> <--project=PROJECT>
pipenv run python toronto/toronto.py instances list
pipenv run python toronto/toronto.py  volumes list

#Install click
pipenv install click


