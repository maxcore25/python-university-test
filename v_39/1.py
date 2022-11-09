from math import *


def main(x):
    a = 79 * floor(x)
    b = (log(x, 2) ** 3) / 45
    c = 54 * log(x ** 2 + x + x ** 3, 2) ** 4

    return "%.2e" % (a - b + c)


print(main(0.33))
print(main(0.44))
print(main(0.73))
print(main(0.72))
print(main(0.92))
