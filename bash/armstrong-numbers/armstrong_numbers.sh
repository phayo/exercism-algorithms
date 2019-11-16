#!/usr/bin/env bash
chmod u+x armstrong_numbers.sh

  main () {
    number=$1
    len=${#number}
    sum=0
    for (( i=0; i<${#number}; i++ )); do
        num="${number:$i:1}"
        
        a=$(($num+0))
        mul=1
        b=$len
        power=0
        while (($b != 0)) 
        do
            mul=$(($mul * $a))
            b=$((b - 1))
        done
        sum=$(( $mul + $sum ))
        
    done
    chk=$(( $number + 0))
    if (($sum == $chk)); then
        echo "true"
    else
        echo "false"
    fi
  }

  # call main with all of the positional arguments
  main "$@"
