part_zero = [1989, 2000, 1964]
part_one = [2020, 2008]
part_two = ['HAML', 'JSON5', 'NSIS']
part_three = [1975, 2012]


def main(x):
    if x[3] == 1989:
        if x[1] == 2020:
            if x[2] == 'HAML':
                return 0
            elif x[2] == 'JSON5':
                return 1
            elif x[2] == 'NSIS':
                if x[0] == 1975:
                    return 2
                elif x[0] == 2012:
                    return 3
        if x[1] == 2008:
            if x[2] == 'HAML':
                return 4
            elif x[2] =='JSON5':
                return 5
            elif x[2] == 'NSIS':
                if x[0] == 1975:
                    return 6
                elif x[0] == 2012:
                    return 7
    elif x[3] == 2000:
        return 8
    elif x[3] == 1964:
        return 9


print(main([1975, 2008, 'NSIS', 1964, 1973]))
print(main([1975, 2008, 'NSIS', 1989, 1973]))
print(main([1975, 2020, 'HAML', 1989, 2012]))
print(main([1975, 2008, 'JSON5', 2000, 1973]))
print(main([1975, 2008, 'JSON5', 1989, 2012]))
