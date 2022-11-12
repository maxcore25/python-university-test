import math


def main(z, x, y):
    a = 24*math.tan(x**3-z-12*y**2)**4-81*x**9
    b = 51*(x**2+60*y**3+z)**6+math.asin(z)
    c = 14*x**9-(y**3+61*z**2)/49
    d = 92*math.log(14*y**2, 2)**3+math.log((x**2/95)+88*z+0.01)**6
    return "%.2e" % (math.sqrt(a/b)+math.sqrt(c/d))


print(main(0.76, 0.74, -0.28))
