#!/usr/bin/env bash
chmod u+x pangram.sh

  main () {
    # your main function code here
    str=$1
    str="${str,,}"
    for letter in {a..z} ; do
        if ! [[ $str == *$letter* ]]; then
            echo false
            exit 0  
        fi
    done
    echo true
    exit 0
  }

  # call main with all of the positional arguments
  main "$@"

