#!/usr/bin/env bash
chmod u+x raindrops.sh


  main () {
    # your main function code here
    num=$1
    if (($num % 105 == 0 )); then
        echo "PlingPlangPlong"
        exit 0
    elif (( $num % 35 == 0 )); then
        echo "PlangPlong"
        exit 0
    elif (( $num % 21 == 0 )); then
        echo "PlingPlong"
        exit 0
    elif (( $num % 15 == 0 )); then
        echo "PlingPlang"
        exit 0
    elif (($num % 7 == 0 )); then
        echo "Plong"
        exit 0
    elif (($num % 5 == 0)); then
        echo "Plang"
        exit 0
    elif (($num % 3 == 0)); then
        echo "Pling"
        exit 0
    else
        echo $num
        exit 0
    fi
  }

  # call main with all of the positional arguments
  main "$@"
