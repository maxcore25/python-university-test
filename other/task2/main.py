import math


def main(x):
    if x < 8:
        return "%.2e" % ((x**2) / 30)
    elif 8 <= x < 77:
        return "%.2e" % ((x/13)**7 + 18*(1+51*x+56*x**2) + 61*x**4)
    elif 77 <= x < 97:
        return "%.2e" % (math.cos(93*x+x**3+69*x**2))
    elif 97 <= x < 196:
        return "%.2e" % ((x/62) + (math.fabs(x))**4)
    elif 196 <= x:
        return "%.2e" % (((x**2-93-x**3)**3) + (((x**3)/93)**5) + (math.fabs(x))**4)


print(main(39))
print(main(-50))
