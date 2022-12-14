import math


def main(x, z, y):
    res = 0
    n = len(x)
    for i in range(1, n + 1):
        a = 97 * y[i - 1] ** 2
        b = 24 * z[n - i]
        c = x[math.ceil(i / 2) - 1] ** 3
        res += 13 * (a - b - c)
    return "%.2e" % res


print((main([-0.73, -0.22, 0.64, -0.58, 0.71, 0.1, -0.46, -0.08],
            [-0.24, 0.4, -0.42, 0.7, -0.27, -0.09, 0.2, -0.35],
            [0.39, 0.31, -0.63, 0.76, 0.93, 0.33, -0.63, 0.75])))
print((main([-0.67, 0.13, 0.41, -0.91, 0.04, -0.3, -0.15, 0.0],
            [-0.52, -0.56, 0.11, -0.52, 0.95, -0.86, -0.73, -0.99],
            [0.2, 0.28, 0.11, -0.12, -0.94, 0.19, 0.49, -0.44])))
print((main([-0.12, 0.46, -0.5, -0.86, 0.34, 0.29, 0.64, -0.73],
            [0.18, -0.87, -0.51, 0.6, -0.96, 0.05, 0.87, -0.15],
            [-0.59, -0.92, 0.64, 0.83, -0.46, 0.94, 0.06, 0.13])))
print((main([-0.91, 0.11, -0.28, 0.85, 0.9, 0.19, -0.43, 0.37],
            [-0.27, 0.69, -0.85, 0.12, -0.91, -0.08, 0.31, 0.79],
            [-0.83, 0.11, -0.2, -0.36, 0.96, 0.38, -0.98, 0.13])))
print((main([0.95, -0.52, 0.73, -0.35, 0.19, -0.43, -0.09, 0.65],
            [0.46, 0.03, 0.05, -0.23, 0.01, -0.82, -0.08, 0.97],
            [0.76, -0.41, 0.64, 0.14, 0.01, -0.34, 0.09, -0.04])))
