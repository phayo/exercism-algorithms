# importing regular expression libary
import re

# defining allowed characters

def is_isogram(string):
    if string == "":
        return True
    # get all alphabetical letters in the given string
    wt = "".join(x.lower() for x in string if x.isalpha())
    for i in range(len(wt)):
        if wt[i] in wt[i+1:]:
            return False
    return True

print(is_isogram("Emily Jung Schwartzkopf"))