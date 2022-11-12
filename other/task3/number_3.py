import math


def main(a, p, b, n, m):
    res1 = 1
    res2 = 0
    for k in range(1, a + 1):
        temp = 50*math.log(p+p**3, 10)-(((60*k**2)**6)/45)-k**4
        res1 *= temp
    for c in range(1, m + 1):
        for j in range(1, n + 1):
            for i in range(1, b + 1):
                temp = (c+28*p**2)**2-j**4-53*i**3
                res2 += temp
    return "%.2e" % (res1 + res2)


print(main(8, 0.5, 6, 5, 4))
print(main(2, 0.07, 4, 7, 5))
print(main(3, 0.36, 6, 4, 5))
