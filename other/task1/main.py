import math


def main(z):
    a = math.sqrt((3*z**6 - (63 * z**3)**3) / ((math.cos(z))**2))
    b = math.sqrt(33 * (math.cos(z))**3)
    return "%.2e" % (a - b)


print(main(-0.0))
print(main(-0.17))
