from math import *


def main(z, y, x):
    a = y ** 2 / 75 - 36 * exp(x - 34 * z ** 3 - 1) ** 7
    b = 33 * (abs(x + z ** 2) ** 3) - atan(40 * z + z ** 3 / 11 + y ** 2)
    c = 15 * (76 * x ** 3 - 70 - y ** 2) ** 4 + 71 * (sqrt(z)) ** 7

    return '%.2e' % (sqrt(a / b) + c)


print(main(0.37, 0.84, 0.43))
print(main(0.32, -0.5, 0.36))
print(main(0.17, 0.08, -0.93))
print(main(0.73, -0.34, 0.56))
print(main(0.78, 0.25, 0.85))
