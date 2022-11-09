from math import *


def main(x, y):
    total = 0
    n = len(x)

    for i in range(1, n + 1):
        total += (y[ceil(i / 3) - 1] ** 3 + 52 + 91 * x[ceil(i / 3) - 1]) ** 6

    return 39 * total


print(main([0.32, -0.06, 0.65],
           [-0.4, -0.23, -0.7]))
print(main([-0.27, -0.03, -0.41],
           [-0.62, 0.42, -0.51]))
print(main([-0.92, -0.58, -0.79],
           [0.89, 0.37, -0.87]))
print(main([-0.7, 0.26, -0.74],
           [-0.61, 0.79, -0.45]))
print(main([-0.88, 0.43, -0.92],
           [0.68, 0.25, -0.64]))
