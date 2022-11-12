import math


def main(a, m, b):
    res = 0
    for i in range(1, b + 1):
        for c in range(1, m + 1):
            for k in range(1, a + 1):
                res += math.log(k)**2-i**6-91*(math.fabs(i**2-c-88))**7
    return "%.2e" % res


print(main(6, 4, 8))
print(main(3, 8, 8))
print(main(2, 2, 2))
print(main(2, 7, 5))
print(main(3, 7, 5))
