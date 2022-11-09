from math import *


def main(n):
    if n == 0:
        return -0.77
    if n == 1:
        return -0.24

    return main(n - 2) ** 3 - sin(main(n - 1)) / 63 - 1


print(main(6))
print(main(2))
print(main(7))
print(main(5))
print(main(8))
