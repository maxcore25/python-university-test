import math


def main(z):
    if z < -37:
        return "%.2e" % (53 * math.ceil(50 * z ** 3 + z ** 2 + z / 18))
    elif -37 <= z < 28:
        return "%.2e" % (60*z)
    elif z >= 28:
        return "%.2e" % ((54-24*z-z**2)**3/67)


print(main(-3))
print(main(-25))
print(main(-54))
print(main(22))
print(main(110))
