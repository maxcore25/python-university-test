import math


def main(y):
    return "%.2e" % (((20*y)/((92*y+4*y**2+1)**4+((y/90)-1)**2))+(math.tan(y+y**2+1))**4)


print(main(-0.66))
