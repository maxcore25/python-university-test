import math


def main(x):
    if x < 73:
        return 88*x**2-(52*x**2)**6
    elif 73 <= x < 134:
        return math.log(x, 10)**4/9-18*x-6*(67*x**2-x-x**3)**6
    elif 134 <= x < 178:
        return x**5-1
    elif 178 <= x < 275:
        return 76+41*(6*x**3+14*x)**4
    elif x >= 275:
        return 52*x**2+(94-80*x**3)**4+(x**2/85+5*x**3)**6
