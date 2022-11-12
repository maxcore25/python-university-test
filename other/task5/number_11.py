import math


def main(z, y):
    res = 0
    n = len(y)
    for i in range(1, n + 1):
        a = 18 * z[math.ceil(i / 4) - 1] ** 3
        b = y[n - math.ceil(i / 4)] ** 2
        res += (a + 1 + b) ** 6
    return "%.2e" % (94 * res)


print(main([-0.39, 0.78],
           [0.41, -0.61]))
print(main([0.1, 0.89],
           [-0.25, -0.58]))
print(main([-0.29, 0.8],
           [-0.22, 0.07]))
print(main([0.92, -0.79],
           [-0.89, 0.61]))
print(main([-0.42, 0.13],
           [-0.51, -0.14]))
