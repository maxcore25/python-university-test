part_zero = ['MQL5', 'ABNF']
part_one = [1968, 2012]
part_two = [1967, 1970, 1957]
part_three = [1971, 2007]
part_four = ['XSLT', 'QML', 'HY']


def main(x):
    if x[1] == 1968:
        if x[0] == 'MQL5':
            if x[2] == 1967:
                if x[4] == 'XSLT':
                    return 0
                elif x[4] == 'QML':
                    return 1
                elif x[4] == 'HY':
                    return 2
            elif x[2] == 1970:
                return 3
            elif x[2] == 1957:
                if x[3] == 1971:
                    return 4
                elif x[3] == 2007:
                    return 5
        elif x[0] == 'ABNF':
            return 6
    elif x[1] == 2012:
        if x[2] == 1967:
            return 7
        elif x[2] == 1970:
            return 8
        elif x[2] == 1957:
            return 9


print(main(['MQL5', 2012, 1957, 2007, 'XSLT']))
print(main(['MQL5', 2012, 1970, 1971, 'XSLT']))
