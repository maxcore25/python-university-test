dict1 = {'ASP': 0, 'RUST': 1, }
dict2 = {'NSIS': 3, 'PIC': 4, }
dict3 = {2004: 6, 1987: 7, 1996: 8}
dict4 = {'ASP': 9, 'RUST': 10, }


def main(x):
    if x[1] == 'PLSQL':
        if x[2] == 2004:
            return dict1[x[3]]
        elif x[2] == 1987:
            return 2
        elif x[2] == 1996:
            return dict2[x[0]]
    elif x[1] == 'LEAN':
        if x[3] == 'ASP':
            return 5
        elif x[3] == 'RUST':
            return dict3[x[2]]
    elif x[1] == 'PUG':
        return dict4.get(x[3])


print(main(['PIC', 'PUG', 1987, 'RUST']))
print(main(['PIC', 'LEAN', 1987, 'RUST']))
print(main(['PIC', 'LEAN', 1987, 'ASP']))
print(main(['NSIS', 'PLSQL', 1987, 'ASP']))
print(main(['NSIS', 'PLSQL', 1996, 'ASP']))
