from math import *


def main(n):
    if n == 0:
        return 0.08
    if n == 1:
        return 0.35

    return 1 + main(n - 2) ** 2 / 3 + main(n - 1) ** 3 / 76


print(main(7))
print(main(5))
print(main(9))
print(main(2))
print(main(4))
