import math


def main(y):
    summa = 0
    n = len(y)
    for i in range(1, n+1):
        a = 35*y[n-i]
        b = y[n-math.ceil(i/3)]**2
        summa += (a+b+1)**3
    return "%.2e" % (66 * summa)


print(main([-0.2, -0.67, -0.43, 0.91, -0.17]))
print(main([-0.7, 0.59, -0.57, -0.6, -0.08]))
print(main([-0.97, 0.91, 0.84, -0.51, 0.93]))
