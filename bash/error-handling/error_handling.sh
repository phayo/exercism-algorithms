#!/usr/bin/env bash

chmod u+x error_handling.sh

if [[ $# = 1 ]]; then
    echo "Hello, $1"
    exit 0
else
    echo "Usage: ./error_handling <greetee>"
    exit 1
fi
