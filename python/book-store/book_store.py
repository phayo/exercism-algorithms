price = 800
discounts = {
    "1": 0,
    "2": 5,
    "3": 10,
    "4": 20,
    "5": 25
}

def group(basket):
    matches=[[basket[0]]]
    for i in range(1, len(basket)):
        book = basket[i]
        for j in range(len(matches)):
            if not book in matches[j]:
                matches[j].append(book)
                break
            if j == len(matches) - 1:
                matches.append([book])
                break
    return matches

def balance(groups):
    print(groups)
    den = len(groups)
    if (den % 2 == 1):
        return []
    lenSum = 0
    for group in groups:
        lenSum += len(group)
    avg = lenSum // den
    tmp = []
    more = [group for group in groups if len(group) > avg]
    less = [group for group in groups if len(group) <= avg]
    for i in range(len(more)):
        for j in range(len(more[i])):
            if not i >= len(less):
                if len(less[i]) < avg:
                    if not more[i][j] in less[i]:
                        less[i].append(more[i][j])
                        del more[i][j]
    result = [more, less]
    print(result)
    return [group for bigGroup in result for group in bigGroup]

def calcPrice(basket):
    if (len(basket) == 0):
        return 0
    total = 0
    def discontAmt(discount):
        return (discount / 100) * price
    for group in basket:
        l = len(group)
        d = discontAmt(discounts[str(l)])
        res = l * (price - d)
        #print(f"{total} + {res}")
        total += res
    print(total)
    return int(total)

def total(basket):
    if len(basket) == 0:
        return 0
    normal = calcPrice(group(basket))
    print()
    balanced = calcPrice(balance(group(basket)))
    if normal < balanced or balanced == 0:
        return normal
    else:
        return balanced

    


print(total([1, 1, 2, 2, 3, 3, 4, 4, 5]))