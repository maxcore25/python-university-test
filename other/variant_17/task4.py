import math


def main(n):
    if n == 0:
        return 0.79
    elif n >= 1:
        return 6*main(n-1)**2/42-math.ceil(main(n-1))**3-main(n-1)**2


print(main(4))
print(main(5))
print(main(3))
print(main(1))
print(main(8))
