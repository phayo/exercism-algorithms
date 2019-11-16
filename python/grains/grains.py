
# function to validate user input in list of valid squares
def validate(number):
    if not 0 < number <= 64:
        raise ValueError("Invalid input!")

# function to get the number at a particular square
def square(number):
    validate(number)
    return 2 ** (number - 1)


# to get total sum from the firt square up to a particular square (number)
def total(number):
    validate(number)
    return sum(square(i + 1) for i in range(number))