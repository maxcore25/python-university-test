import math


def main(a, m, b):
    res = 0
    for k in range(1, b + 1):
        for j in range(1, m + 1):
            for c in range(1, a + 1):
                res += 18*(j**2-c**3/34)**5+k**6
    return "%.2e" % res


print(main(6, 3, 3))
print(main(3, 5, 4))
print(main(6, 6, 7))
print(main(6, 6, 5))
print(main(5, 8, 5))
