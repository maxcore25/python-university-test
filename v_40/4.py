from math import *


def main(n):
    if n == 0:
        return -0.52
    if n == 1:
        return -0.23

    return sin(main(n - 2) ** 2) ** 2 - main(n - 1)


print(main(9))
print(main(7))
print(main(4))
print(main(5))
print(main(6))
