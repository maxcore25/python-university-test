import math


def main(b, x, m):
    res1 = 0
    for i in range(1, b + 1):
        res1 += (i**2/82+1+x**3)**4/23-84*i**9
    res2 = 0
    for k in range(1, m + 1):
        for c in range(1, b + 1):
            res2 += 13*math.floor(c)**5+c**3+80*k**2
    return res1-res2


print(main(2, 0.63, 7))
print(main(4, -0.82, 8))
print(main(7, -0.75, 2))
print(main(2, -0.57, 4))
print(main(7, 0.89, 8))
