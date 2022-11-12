import math


def main(x):
    n = len(x)
    res = 0
    for i in range(1, n + 1):
        res += math.sqrt(27*x[n-math.ceil(i/2)]**3)**3
    return 50*res
