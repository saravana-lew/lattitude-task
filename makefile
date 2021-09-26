SHELL:=/bin/bash

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