import re
bad = '[@:! )-.(+]'
forbidden = ['0', '1']

class Phone(object):
    def __init__(self, phone_number):
        self.number = phone_number
        self.number = self.check()
        self.area_code = self.number[:3]
        
    def check(self):
        self.number = re.sub(bad, '', self.number)

        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]

        if not len(self.number) == 10:
            raise ValueError("Invalid phone number")
        
        if not self.number[0] in forbidden and not self.number[3] in forbidden:
            return self.number
        else:
            raise ValueError("Invalid phone number")
    
    def pretty(self):
        return "({}) {}-{}".format(self.number[:3], self.number[3:6], self.number[6:])

if __name__=="__main__":
    print(Phone("+1 (223) 456-7890").number)