#!/usr/bin/env bash

chmod u+x leap.sh

main () {
  year=$1
  c=$#


  if (( $c != 1 )); then
    echo 'Usage: leap.sh <year>'
    exit 1
  fi

  re='^[0-9]+$'
  if ! [[ $year =~ $re ]] ; then
    echo 'Usage: leap.sh <year>'; exit 1
  fi

  if [[ $number =~ ^[+-]?[0-9]+\.?[0-9]*$ ]];then
    echo 'Usage: leap.sh <year>'; exit 1
  fi

  res="false"
    # your main function code here
  if (($year % 4 == 0)); then
    if (($year % 100 == 0)) && (($year % 400 != 0)); then
      res="false";
    else
      res="true"
    fi
  else
    res="false";
  fi
  echo $res
}

  # call main with all of the positional arguments
  main "$@"

