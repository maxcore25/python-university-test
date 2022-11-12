import math


def main(z, x, y):
    a = 19*math.tan(y)**5+23*math.sqrt(z**3-1-53*x)**7
    b = math.fabs(y+24+(y**3/90))+(25*x**3+z**2+85)**3
    c = 96*(math.fabs((y/61)+1+39*z**2))**5-x**3
    return "%.2e" % (a-(b/c))


print(main(0.47, -0.38, -0.8))
