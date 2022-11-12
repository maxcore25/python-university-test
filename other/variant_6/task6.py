part_zero = ['SLIM', 'C', 'RDOC']
part_one = [1990, 2014, 1995, 1960, 1991, 2000]
part_two = [2000, 1957, 2000, 1957, 1990, 2014, 1995]


def main(x):
    if x[2] == 'SLIM':
        if x[3] == 1990:
            if x[0] == 2000:
                return 0
            elif x[0] == 1957:
                return 1
        elif x[3] == 2014:
            return 2
        elif x[3] == 1995:
            return 3
    elif x[2] == 'C':
        return 4
    elif x[2] == 'RDOC':
        if x[1] == 1960:
            if x[0] == 2000:
                return 5
            elif x[0] == 1957:
                return 6
        elif x[1] == 1991:
            if x[3] == 1990:
                return 7
            elif x[3] == 2014:
                return 8
            elif x[3] == 1995:
                return 9
        elif x[1] == 2000:
            return 10


print(main([2000, 1960, 'SLIM', 1990]))
print(main([1957, 1960, 'SLIM', 1990]))
print(main([2000, 2000, 'C', 2014]))
print(main([1957, 1991, 'RDOC', 1995]))
print(main([1957, 1991, 'RDOC', 1990]))
