import math


def main(n):
    if n == 0:
        return 0.67
    elif 1 <= n:
        return math.log(28 * (main(n - 1) ** 3) + 14 + (main(n - 1)) ** 2) ** 3


print(main(6))
print(main(8))
