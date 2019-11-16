#!/usr/bin/env bash
chmod u+x bob.sh

  isUpper(){
    str=$1
    regexp="/[a-z]/i"
    # echo $regexp
    uppr=${str^^}
    # print $uppr
    if [[ $str =~ [a-z] ]]; then
      # print "here"
      if [[ $str == $uppr ]]; then
        local upp="true"
        echo $upp
      else
        local upp="false"
        echo $upp
      fi
    else
      local upp="true"
      echo $upp
    fi
  }

  main () {
    # your main function code here
    str=$1
    # string=${sed 's/\s+//g' $str}
    string=${str//[[:space:]]/}
    count=${#string}
    last="${string: -1}"
    que="\?"
    upper=$(isUpper "$string")
    echo $string
    # echo $que
    if [[ $upper == "true" ]] && [[ $last == $que ]]; then
      echo "Calm down, I know what I'm doing!"
    elif  [[ $upper == "true" ]]; then
      echo "Whoa, chill out!";
    elif [[ $last == $que ]]; then
      echo "Sure."
    elif [[ $count == 0 ]]; then
      echo "Fine. Be that way!"
    else
      echo "Whatever."
    fi
  }

  # call main with all of the positional arguments
  main "$@"

