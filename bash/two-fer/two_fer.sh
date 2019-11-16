#!/usr/bin/env bash

chmod u+x two_fer.sh

if [[ $# = 0 ]]; then
    bat="One for you, one for me."
else
    bat="One for $1, one for me."
fi
echo $bat
exit 0
