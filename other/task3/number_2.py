import math


def main(a, n, b):
    res = 1
    for c in range(1, b + 1):
        for k in range(1, n + 1):
            temp = 0
            for i in range(1, a + 1):
                temp += (c - 43*(math.fabs(i - 27*k**2))**6-1)
            res *= temp
    return "%.2e" % res


print(main(7, 3, 3))
print(main(3, 3, 7))
print(main(3, 7, 8))
