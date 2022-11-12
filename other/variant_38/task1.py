import math


def main(x):
    a = math.sqrt(80*x)
    b = 70*(23+12*x**3)**7
    c = (x**2-64*x**3-x)**3/15
    return a - (b + c)


