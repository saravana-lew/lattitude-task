#!/bin/bash


# Process script parameters
case "$1" in
    build)
        #build commmad
    ;;
    test)
        python3 -m unittest discover -s ./tests/unit/ -p '*.py'
    ;;
    deploy)
       ## Deployment command
    ;;
    -*)
        echo "Unknown operation: $1"
        exit 1
    ;;
esac
