import math


def main(x, z, y):
    a = 81-(x-y**2-95*z**3)**2/30
    b = (1+x**2+z**3)**7+(0.02+y**2+x**3)**6/24
    c = 71*z**7+(1+y**2+29*x)**5
    return "%.2e" % (math.sqrt(a)-b/c)


print(main(0.57, 0.25, -0.84))
print(main(0.38, 0.7, 0.52))
print(main(0.15, 0.13, -0.66))
print(main(0.07, -0.79, -0.8))
print(main(-0.31, 0.7, 0.45))
