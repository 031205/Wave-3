n = input('Enter an integer (2 or greater): ')
n = int(n)
if n >= 2:
    print('The prime factors of',n,'are:')
    factor_list = []
    factor = 2
    while factor <= n:
        if n % factor == 0:
            n = n / factor
            factor_list.append(factor)
        else:
            factor = factor + 1
    for i in factor_list:
        print(i)
else:
    print('This number is invalid.')



