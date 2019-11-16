import re

def count_words(sentence):
    sentence = sentence.lower()
    words = set(re.findall('[a-z0-9]+(?:\'[a-z0-9])*(?:[a-z0-9]+)*', sentence))
    result = dict()
    # splitted = re.split("\s|\.|'|_", sentence)
    # print(splitted)
    sentence = re.sub('\_', ' ', sentence)
    print(sentence)
    for word in words:
        num = len(re.findall('\\b'+word+'\\b', sentence))
        result[word] = num
    return result


print(count_words("this is the part_icula definition's of a sentence"))