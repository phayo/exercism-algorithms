import re

class Luhn(object):
    def __init__(self, card_num):
        self.card = re.sub('[\s]', '', card_num)

    def valid(self):
        if not self.card.isdigit() or len(self.card) == 1:
            return False
        card_reversed = self.card[::-1]
        even_sum = 0
        odd_sum = sum([int(card_reversed[i]) for i in range(len(card_reversed)) if i % 2 == 0])
        eSum = [int(card_reversed[i]) * 2 for i in range(len(card_reversed)) if not i % 2 == 0]
        
        for num in eSum:
            if num >= 10:
                num = num - 9
                even_sum += num
            else:
                even_sum += num
        return (odd_sum + even_sum) % 10 == 0


number = Luhn("234 567 891 234")
print(number.valid())