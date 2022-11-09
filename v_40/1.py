from math import *


def main(z, x, y):
    a = floor(64 * y + 56 * z ** 3 + 94) \
        - (15 * z ** 2 + 38 * x ** 3) ** 6
    b = 83 * z ** 6 - 54 * (x - y ** 3) ** 2
    c = 96 * (sin(y ** 3 / 57 - 4 * z ** 2)) ** 4
    d = (1 + 48 * y ** 3 + 89 * x ** 2) ** 7

    return "%.2e" % (sqrt(a) - b / (c - d))


print(main(0.2, -0.22, 0.84))
print(main(0.66, -0.61, 0.51))
print(main(-0.17, 0.19, 0.39))
print(main(0.4, -0.43, 0.25))
print(main(0.03, 0.23, -0.07))
