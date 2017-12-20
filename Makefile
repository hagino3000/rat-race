.PHONY: info setup packages

PYTHON:=./env/bin/python
PIP:=./env/bin/pip


info:
	$(PYTHON) --version
	$(PIP) --version

env:
	virtualenv --python /usr/bin/python3.6 ./env

packages:
	$(PIP) install -r ./requirements.txt

setup: env packages
	$(PIP) install -e .
