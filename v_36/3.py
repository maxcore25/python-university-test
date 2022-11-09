from math import *


def main(a, m, z):
    res = 1

    for j in range(1, m + 1):
        it_sum = 0
        for i in range(1, a + 1):
            it_sum += \
                (i + 25 * j ** 2 + 39) ** 2 + \
                26 * z ** 4 + (floor(14 * i + 39)) ** 6
        res *= it_sum

    return '%.2e' % res


print(main(6, 2, 0.31))
print(main(5, 8, 0.85))
print(main(5, 6, -0.83))
print(main(5, 4, -0.26))
print(main(4, 4, 0.68))
