import math


def main(z):
    if z < 140:
        return "%.2e" % (92*math.sin(z))
    elif 140 <= z < 175:
        return "%.2e" % ((z**2+(z**3/17))**2)
    elif 175 <= z < 231:
        return "%.2e" % (z**4-12*z**3)
    elif 231 <= z < 256:
        return "%.2e" % (39*math.log(z, 2)**3)
    elif z >= 256:
        return "%.2e" % (7*z**4)


print(main(332))
print(main(285))
print(main(239))
print(main(184))
print(main(219))
