import math


def main(n):
    if n == 0:
        return -0.16
    if n == 1:
        return 0.81
    if n >= 2:
        return math.sin(79*main(n-2)-10*main(n-2)**3-main(n-1)**2)
