import math


def main(x):
    if 38 > x:
        return "%.2e" % (45*math.atan(96*x)**7-x-0.02)
    elif 128 > x >= 38:
        return "%.2e" % (38*math.sin(x)**6+26*(math.fabs(x))**7+x**2)
    elif 159 > x >= 128:
        return "%.2e" % (x**2+52*x**5+x**3)
    elif x >= 159:
        return "%.2e" % (20*((x/39)+11*x**3)**3-x**14)


print(main(76))
