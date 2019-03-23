def numberIsPrime(number):
    isPrime = True
    for x in range(2, 9):
        if number != x:
            if number % x == 0:
                isPrime = False
                break
    if isPrime == True:
        return True
    elif isPrime == False:
        return False

for x in range (1, 10000):
    if numberIsPrime(x) == True:
        print(x)