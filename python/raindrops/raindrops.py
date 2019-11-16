def convert(number):
    if number % 105 == 0:
        return 'PlingPlangPlong'
    elif number % 35 == 0:
        return 'PlangPlong'
    elif number % 21 == 0:
        return 'PlingPlong'
    elif number % 15 == 0:
        return 'PlingPlang'
    elif number % 7 == 0:
        return 'Plong'
    elif number % 5 == 0:
        return 'Plang'
    elif number % 3 == 0:
        return 'Pling'
    else:
        return str(number)
