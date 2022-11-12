import math


def main(n, m, z):
    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            res += 28*j-66*(94*i+62*z**3+z**2)**7
    return res

print(main(4, 7, -0.15))
