def factors(value):
    res = []
    n = 2
    while not value <= 1:
        if value % n == 0:
            res.append(n)
            value =  value // n
        else:
            n += 1
    return res
    
if __name__=="__main__":
    print(factors(64))