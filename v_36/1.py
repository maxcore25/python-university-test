from math import *


def main(x, y):
    a = 36 * x ** 3 - y ** 4
    b = (x ** 2 - x ** 3 - 47 * y) ** 2
    c = 19 * (x ** 3 + y ** 2) ** 3 - (sqrt(6 * x + 63)) ** 7
    d = acos(y + 56 * x ** 3) ** 7 + y

    return "%.2e" % (a / b + c / d)


print(main(0.13, -0.36))
print(main(-0.03, -0.59))
print(main(-0.19, -0.22))
print(main(0.12, 0.63))
print(main(0.07, -0.25))
