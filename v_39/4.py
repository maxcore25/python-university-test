from math import *


def main(n):
    if n == 0:
        return 0.35
    if n == 1:
        return 0.49

    return main(n - 1) - \
        64 * tan(main(n - 2) ** 3 - main(n - 2) ** 2 / 31) ** 3


print(main(3))
print(main(6))
print(main(5))
print(main(9))
print(main(2))
