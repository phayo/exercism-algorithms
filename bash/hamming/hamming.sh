#!/usr/bin/env bash
chmod u+x hamming.sh

  main () {
    # your main function code here
    c=$1
    d=$2
    l=${#2}
    dist=0
    for (( i=0; i<$l; i++ )); do
        if [ "${c:$i:1}" == "${d:$i:1}" ]; then
            continue
        else
            dist=$((dist + 1))
        fi
    done
    echo $dist
    exit 0
  }

  # call main with all of the positional arguments
  if (($# == 2)) ; then
    if ((${#1} == ${#2})); then
        main "$@"
    else
        echo "left and right strands must be of equal length"
        exit 1
    fi
  else
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
  fi
