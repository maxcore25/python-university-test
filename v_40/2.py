from math import *


def main(x):
    if x < 23:
        return 39 * (ceil(x)) ** 5 - 39 * (17 * x ** 2 + 53 * x + 80) ** 4
    if 23 <= x < 59:
        return atan(61 * x ** 3) ** 5 + 1
    if 59 <= x < 138:
        return x ** 7
    if 138 <= x < 237:
        return (x ** 3 - 43 * x ** 2) ** 7

    return (x ** 2 - 1 - x ** 3) ** 4 + 45 * (x + 68 + x ** 2 / 13) + \
        asin(x ** 2 + 87 + x ** 3) ** 3


print(main(138))
print(main(86))
print(main(8))
print(main(42))
print(main(-57))
