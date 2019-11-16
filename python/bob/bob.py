import re

def response(hey_bob):
    isUpper=hey_bob.isupper()
    no_space = len(re.sub(r"\s*", "", hey_bob)) > 0
    question= no_space and hey_bob.strip()[-1] == '?'

    if(isUpper and question):
        return "Calm down, I know what I'm doing!"
    elif (isUpper):
        return 'Whoa, chill out!'
    elif (question):
        return 'Sure.'
    elif (not no_space):
        return "Fine. Be that way!"
    else:
        return "Whatever."
