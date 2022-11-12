import math


def f(y):
    if y < 85:
        return "%.2e" % (78*(y**2-y**3)**7-39*y-28*(15+40*y**3+23*y)**5)
    elif 85 <= y < 130:
        return "%.2e" % (y**6+54*y**3+85*(y+1)**2)
    elif 130 <= y < 171:
        return "%.2e" % (y**2/92-y**3)
    elif 171 <= y < 244:
        return "%.2e" % (y**2/54-(81*y**2+82*y**3+0.04)**7/45)
    elif y >= 244:
        return "%.2e" % (25*y**4-82*(0.01+y**3+77*y)**3-0.01)


print(f(9))
print(f(271))
print(f(23))
print(f(288))
print(f(31))
