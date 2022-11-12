from math import *


def main(a, m):
    res = 1

    for c in range(1, m + 1):
        it_sum = 0
        for k in range(1, a + 1):
            it_sum += (c ** 7 / 65 - 24 * (71 - k ** 3 - k ** 2) ** 3 - k ** 6 / 50)
        res *= it_sum

    return '%.2e' % res


print(main(2, 3))
print(main(2, 7))
print(main(7, 7))
print(main(5, 3))
print(main(3, 3))
