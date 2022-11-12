import math


def main(z):
    summa = 0
    for i in range(0, 7):
        summa += math.exp(65+78*(z[i // 4]**2)+93*z[i // 4])
    return "%.2e" % (47 * summa)


print(main([0.99, 0.21, -0.82, 0.53, 0.65, -0.29, -0.83]))
print(main([-0.17, 0.08, -0.22, -0.58, 0.52, -0.51, -0.14]))
