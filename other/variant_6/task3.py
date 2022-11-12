import math


def f(a, b, n, m):
    res1 = 0
    res3 = 1
    for j in range(1, b + 1):
        for i in range(1, a + 1):
            res1 += math.tan(i)**2-(j**2+j**3)**5/34
    for c in range(1, b + 1):
        for k in range(1, m + 1):
            res2 = 0
            for i in range(1, n + 1):
                res2 += (3*c**3+i**2/63)**3/80+k**6
            res3 *= res2
    return "%.2e" % (res1 + res3)


print(f(3, 3, 8, 8))
print(f(7, 8, 5, 2))
print(f(2, 4, 6, 7))
print(f(2, 5, 5, 6))
print(f(8, 4, 8, 5))
