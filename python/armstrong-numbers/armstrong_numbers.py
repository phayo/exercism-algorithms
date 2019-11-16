def is_armstrong_number(number):
    n = len(str(number))
    return number == sum([int(x) ** n for x in str(number)])
