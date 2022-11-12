import math


def main(b, n):
    res1 = 0
    res2 = 0
    for i in range(1, b + 1):
        temp = 1 + (((i/30)-i**2)/10) + (43-i-51*i**2)**2
        res1 += temp
    for i in range(1,  n + 1):
        for j in range(1, b + 1):
            temp = (j**5) - ((j**2)-93-i**3)**4
            res2 += temp

    return "%.2e" % (res1 - res2)


print(main(5, 5))
print(main(2, 8))
