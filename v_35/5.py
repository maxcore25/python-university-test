from math import *


def main(x):
    total = 0
    n = len(x)

    for i in range(1, n + 1):
        total += atan(24 - x[n - i] ** 3 / 92 - 22 * x[i - 1] ** 2) ** 3

    return 97 * total


print(main([0.11, -0.5, -0.67, 0.22, -0.27, -0.86]))
print(main([-0.61, 0.38, 0.2, -0.14, 0.66, 0.19]))
print(main([-0.63, -0.97, 0.73, 0.1, 0.68, 0.03]))
print(main([-0.23, 0.45, -0.51, 0.28, -0.87, 0.01]))
print(main([-0.3, 0.63, -0.98, 0.93, 0.07, -0.32]))
