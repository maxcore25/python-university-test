from math import *


def main(a, m, n):
    res = 0

    for k in range(1, n + 1):
        it_sum = 0
        for j in range(1, m + 1):
            product = 1
            for i in range(1, a + 1):
                product *= \
                    59 + (i / 67 - k ** 3 - j ** 2) ** 2 \
                    + 60 * (k ** 3 + 9 * i) ** 3
            it_sum += product
        res += it_sum

    return '%.2e' % res


print(main(2, 8, 6))
print(main(5, 2, 8))
print(main(6, 4, 2))
print(main(7, 2, 8))
print(main(2, 7, 5))
