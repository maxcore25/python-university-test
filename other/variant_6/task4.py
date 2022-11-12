import math


def f(n):
    if n == 0:
        return -0.71
    elif n == 1:
        return -0.61
    elif n >= 2:
        return math.log(f(n-1)**2/68-f(n-2)/48)


print(f(4))
print(f(9))
print(f(2))
print(f(5))
print(f(3))
