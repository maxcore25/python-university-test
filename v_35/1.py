from math import *


def main(x):
    a = x ** 3
    b = 0.01 - acos(61 * x ** 3 - 55 * x ** 2)
    c = x ** 2 - x ** 3
    d = 88 * (1 + x ** 2 / 20) ** 4 + 53 * x ** 6

    return "%.2e" % (a / b - c / d)


print(main(0.1))
print(main(-0.03))
print(main(0.9))
print(main(0.13))
print(main(0.12))
