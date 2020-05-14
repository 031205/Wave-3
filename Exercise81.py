from math import sqrt


def HypotenuseCalculator(a,b):
    hypotenuse = sqrt(a*a + b*b)
    return hypotenuse


side1 = input('Input the length of the first shorter side of a triangle: ')
side1 = float(side1)
side2 = input('Input the length of the second shorter side of a triangle: ')
side2 = float(side2)
if side1 > 0 and side2 > 0:
    hypotenuse = HypotenuseCalculator(side1,side2)
    print('The length of the hypotenuse of this triangle is',hypotenuse)
else:
    print('Invalid input')