dict1 = {1991: 0, 1963: 1, }
dict2 = {'M4': 2, 'BISON': 3, }
dict3 = {1989: 5, 2012: 6, 1970: 7}
dict4 = {1989: 9, 2012: 10, 1970: 11}


def main(x):
    if x[0] == 'XBASE':
        if x[4] == 'M':
            if x[2] == 'DM':
                return dict1[x[1]]
            return dict2[x[2]]
        elif x[4] == 'DIFF':
            if x[1] == 1991:
                return 4
            return dict3[x[3]]
    elif x[0] == 'URWEB':
        if x[4] == 'M':
            if x[1] == 1991:
                return 8
            return dict4[x[3]]
        return 12


print(main(['URWEB', 1991, 'DM', 2012, 'M']))
print(main(['XBASE', 1991, 'M4', 2012, 'DIFF']))
print(main(['URWEB', 1963, 'DM', 2012, 'M']))
print(main(['XBASE', 1991, 'DM', 2012, 'M']))
print(main(['XBASE', 1963, 'BISON', 1970, 'DIFF']))
