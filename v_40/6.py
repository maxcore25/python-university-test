dict1 = {1996: 0, 1968: 1, }
dict2 = {1996: 2, 1968: 3, }
dict3 = {2020: 4, 2005: 5, 1973: 6}
dict4 = {2020: 8, 2005: 9, 1973: 10}


def main(x):
    if x[0] == 'PONY':
        if x[1] == 1985:
            return dict1[x[3]]
        elif x[1] == 2012:
            return dict2[x[3]]
        elif x[1] == 1966:
            return dict3[x[2]]
    elif x[0] == 'PAN':
        return 7
    elif x[0] == 'IDRIS':
        return dict4.get(x[2])


print(main(['IDRIS', 1985, 2005, 1996]))
print(main(['IDRIS', 2012, 1973, 1968]))
print(main(['PONY', 1966, 1973, 1996]))
print(main(['PONY', 1966, 2020, 1968]))
print(main(['PAN', 1966, 2020, 1996]))
