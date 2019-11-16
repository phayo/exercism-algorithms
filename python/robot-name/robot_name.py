import string
import random
NAMES = []

class Robot(object):
    def __init__(self):
        self.name = self.genName()

    def genName(self):
        alpha = list(string.ascii_uppercase)
        initial = alpha[random.randint(0, 25)] + alpha[random.randint(0, 25)]
        name = "{}{}".format(initial, random.randint(100, 999))
        if name in NAMES:
            return self.genName()
        else:
            NAMES.append(name)
            return name
    
    def reset(self):
        self.name = self.genName()