import math


def main(n):
    if n == 0:
        return -0.75
    if n == 1:
        return 0.11
    if n >= 2:
        return main(n-2)**2-45-main(n-1)


print(main(6))
print(main(2))
print(main(7))
print(main(5))
print(main(4))
