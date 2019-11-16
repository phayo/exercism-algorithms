#!/usr/bin/env bash
chmod u+x acronym.sh

  main () {
    # your main function code here
    IFS=' -*\_'
    read -a strarr <<< $1
    # Print each value of the array by using the loop
    c=1
    output=""
    for val in "${strarr[@]}";
    
    do
        first="$(echo "$val" | head -c 1)"
        [[ -z "${first// }" ]]
        if [ ${#first} -eq 0 ]; then
        # echo here
           continue
        fi
        output+="${first^^}"
        # done
        # printf "$first\n"
    done
    echo $output
  }

  # call main with all of the positional arguments
  main "$@"

