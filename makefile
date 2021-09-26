SHELL:=/bin/bash

#----------------------
# Development
#----------------------

install:
	pip install -r ./src/requirements.txt

install-dev:
	pip install awscli boto3 pytest

#----------------------
# Test
#----------------------
test:
	bash ./bin/run.sh test
#----------------------
# Build
#----------------------
build:
	bash ./bin/run.sh build
#----------------------
# Deploy
#----------------------
deploy:
	bash ./bin/run.sh deploy

.PHONY: build test deploy