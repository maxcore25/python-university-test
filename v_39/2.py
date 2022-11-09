from math import *


def main(x):
    if x < 42:
        return 49 * (floor(x)) ** 2 - log(x, 10) ** 7 - 80 * x ** 5
    if 42 <= x < 56:
        return x ** 2
    if 56 <= x < 139:
        return x ** 4 - 26 - 53 * (52 * x ** 2 - x - 0.01) ** 3
    if 139 <= x < 237:
        return 34 * (x + 1) + (x ** 3 + 1) ** 3 + x ** 7

    return cos(x ** 3 / 81 + 43) ** 2 + x


print(main(218))
print(main(23))
print(main(106))
print(main(201))
print(main(148))
