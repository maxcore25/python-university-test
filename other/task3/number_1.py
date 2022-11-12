import math


def main(a, m, n):
    res1 = 0
    res2 = 0
    for k in range(1, a + 1):
        temp = (1-45*k**3-20*k**2)**7
        res1 += temp
    for i in range(1, n + 1):
        for c in range(1, m + 1):
            temp = 825*c+math.log(91*i**3+c+15)+0.01
            res2 *= temp
    return "%.2e" % (res1+res2)


print(main(8, 3, 3))
print(main(5, 4, 5))
print(main(4, 2, 2))
