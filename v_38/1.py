from math import *


def main(x):
    a = sqrt(80 * x)
    b = 70 * (23 + 12 * x ** 3) ** 7
    c = (x ** 2 - 64 * x ** 3 - x) ** 3 / 15

    return "%.2e" % (a - (b + c))


print(main(0.17))
print(main(0.23))
print(main(0.31))
print(main(0.6))
print(main(0.56))
