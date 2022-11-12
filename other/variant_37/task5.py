import math


def main(z, x):
    n = len(z)
    res = 0
    for i in range(1, n + 1):
        a = 95*z[n-i]**3
        b = z[n-math.ceil(i/2)]
        c = 89*x[n-math.ceil(i/3)]**2
        res += (a + b + c)**4
    return 73 * res
