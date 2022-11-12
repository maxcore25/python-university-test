import math


def main(z, x):
    a = 99*math.cos(79+85*z)**4
    b = (53*x**2-44*x)**5/99
    c = 23*(x**3+15*z)**4
    return "%.2e" % (math.sqrt(a - b) - c)


print(main(0.99, 0.37))
print(main(0.09, 0.3))
print(main(0.75, 0.29))
print(main(-0.15, -0.1))
print(main(-0.81, 0.2))
