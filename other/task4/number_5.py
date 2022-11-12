import math


def main(n):
    if n == 0:
        return 0.83
    if n == 1:
        return 0.53
    if n >= 2:
        return 1 + ((math.atan(main(n - 1) ** 2 - 1 - main(n - 1)) ** 2) / 88) \
               + math.cos(main(n - 2)) ** 3


print(main(3))
print(main(8))
print(main(7))
