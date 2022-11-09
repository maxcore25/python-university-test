import math


def main(x, y):
    a = math.exp(y) ** 7 / 24
    b = 59 * math.log(x, 2) ** 2
    c = 89 * (x ** 3 / 79 + 95 * y + 83) ** 6
    return "%.2e" % (a - b - c)


print(main(0.08, 0.91))
print(main(0.73, -0.61))
print(main(0.78, -0.5))
print(main(0.63, -0.29))
print(main(0.6, 0.84))
