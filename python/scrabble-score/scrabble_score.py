scores = [
    ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    ["D", "G"],
    ["B", "C", "M", "P"],
    ["F", "H", "V", "W", "Y"],
    ["K"],
    ["J", "X"],
    ["Q", "Z"]
    ]

def score(word):

    if word.isalpha():
        word = word.upper()
        score = 0
        for cha in word:
            if cha in scores[0]:
                score += 1
            elif cha in scores[1]:
                score += 2
            elif cha in scores[2]:
                score += 3
            elif cha in scores[3]:
                score += 4
            elif cha in scores[4]:
                score += 5
            elif cha in scores[5]:
                score += 8
            elif cha in scores[6]:
                score += 10
        return score
    else:
        return 0

print(score("abcdefghijklmnopqrstuvwxyz"))


        
