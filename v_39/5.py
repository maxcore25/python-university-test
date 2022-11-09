from math import *


def main(x):
    total = 0
    n = len(x)

    for i in range(1, n + 1):
        total += \
            log((1 + 80 * x[ceil(i / 2) - 1] +
                 x[ceil(i / 2) - 1] ** 3), 2) ** 7

    return total / 39


print(main([0.42, -0.01, 0.01]))
print(main([0.81, 0.91, 0.31]))
print(main([0.36, 0.25, 0.98]))
print(main([0.56, 0.75, -0.86]))
print(main([0.68, 0.73, -0.63]))
