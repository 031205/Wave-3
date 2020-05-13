from Exercise92 import PrimeNumberIndicator


num = input('Input an integer number: ')
num = int(num)
b = PrimeNumberIndicator(num)
if b is True:
    print('It is a prime number.')
elif b is False:
    print('It is not a prime number.')

