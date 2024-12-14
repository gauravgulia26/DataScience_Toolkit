def PrimeNumber(limit):
    if limit == 1:
        return 1
    else:
        for j in range(limit):
            for i in range(2, int(limit**0.5 + 1)):
                if limit % i == 0:
                    return "Number is Not Prime"
                else:
                    return "Number is Prime"


print(PrimeNumber(10))