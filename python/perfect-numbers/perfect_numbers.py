def classify(number):
    if number < 1:
        raise ValueError("{} is not a natural number".format(number))
    factor = sum([x for x in range(1, number) if number % x == 0 ])
    return 'perfect' if number == factor else 'deficient' if number > factor else 'abundant'
    