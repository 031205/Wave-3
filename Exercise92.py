def PrimeNumberIndicator(a):
    if a >= 2:
        for i in range(2,a):
            if a % i == 0:
                return False
        return True
    else:
        return False

