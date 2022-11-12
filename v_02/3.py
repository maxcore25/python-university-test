from math import *


def main(a, n, b):
    res = 0

    for c in range(1, b + 1):
        product = 1
        for k in range(1, n + 1):
            it_sum = 0
            for i in range(1, a + 1):
                it_sum += c - 43 * (floor(i - 27 * k ** 2)) ** 6 - 1
            product *= it_sum
        res += product

    return '%.2e' % res


print(main(7, 3, 3))
print(main(3, 3, 7))
print(main(3, 7, 8))
print(main(4, 4, 5))
print(main(6, 6, 8))
