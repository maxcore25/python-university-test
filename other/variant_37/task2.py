import math


def main(y):
    if y < -19:
        return (y**2-1)**4-72*math.atan(y)**5
    if -19 <= y < 14:
        return 26*math.cos(70*y**3)**3-y**6-y**5
    if 14 <= y < 45:
        return 5*(1+y/28+y**2/77)**3 -\
               (math.fabs(y))**2-(math.floor(44*y**3))**5
    if 45 <= y < 94:
        return (y**3/21)**7-14*(math.ceil(y))**5
    if y >= 94:
        return 21*(30+y/98)**2


print(main(72))
print(main(-42))
print(main(-21))
print(main(119))
print(main(108))
