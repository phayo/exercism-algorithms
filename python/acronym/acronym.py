import re

def abbreviate(words):
    words = re.sub('\_', '', words)
    word_list = re.split('[\s\-\,\_]', words)
    print(word_list)
    tla = "".join([x[0].upper() for x in word_list if not x == ""])
    return tla

print(abbreviate("The Road _Not_ Taken"))