part_one = ['ATS', 'ROFF', 'ABNF']
part_two = ['TEX', 'CSS', 'SLASH', 'SWIFT', 'CIRRU', 'XPROC']
part_three = ['SWIFT', 'CIRRU', 'XPROC', 'TEX', 'CSS', 'SLASH', 2008, 1995, 1982]


def main(x):
    if x[3] == 'ATS':
        if x[1] == 'TEX':
            if x[0] == 'SWIFT':
                return 0
            elif x[0] == 'CIRRU':
                return 1
            elif x[0] == 'XPROC':
                return 2
        elif x[1] == 'CSS':
            return 3
        elif x[1] == 'SLASH':
            return 4
    elif x[3] == 'ROFF':
        return 5
    elif x[3] == 'ABNF':
        if x[0] == 'SWIFT':
            if x[1] == 'TEX':
                return 6
            elif x[1] == 'CSS':
                return 7
            elif x[1] == 'SLASH':
                return 8
        elif x[0] == 'CIRRU':
            if x[2] == 2008:
                return 9
            elif x[2] == 1995:
                return 10
            elif x[3] == 1982:
                return 11
        elif x[0] == 'XPROC':
            return 12


print(main(['XPROC', 'CSS', 1982, 'ATS']))
print(main(['SWIFT', 'SLASH', 1995, 'ABNF']))
print(main(['CIRRU', 'TEX', 2008, 'ROFF']))
print(main(['XPROC', 'TEX', 2008, 'ABNF']))
print(main(['CIRRU', 'TEX', 2008, 'ABNF']))