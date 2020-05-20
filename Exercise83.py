def Shipping_Calculator(num):
    n = 10.95 + (num - 1) * 2.95
    return n


item_num = input('Enter the number of items in the order: ')
item_num = int(item_num)
if item_num > 0:
    shipping_charge = Shipping_Calculator(item_num)
    print('The shipping charge of your order is $',round(shipping_charge,2),sep='')
else:
    print('Ivalid Input')

