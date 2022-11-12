import math


def main(n):
    if n == 0:
        return -0.16
    if n == 1:
        return -0.09
    if n >= 2:
        return (main(n - 1) / 66) + main(n - 2) ** 3


print(main(9))
print(main(5))
print(main(8))
