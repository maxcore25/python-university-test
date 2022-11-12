dict_one = {'J': 0, 'SQL': 1}
dict_two = {2003: 4, 2008: 5, 1973: 6}
dict_three = {2003: 8, 2008: 9, 1973: 10}


def main(x):
    if x[0] == 1997:
        if x[4] == 'EBNF':
            if x[2] == 1987:
                return dict_one.get(x[1])
            return 2
        if x[4] == 'RUST':
            return 3
        if x[4] == 'YANG':
            if x[2] == 1987:
                return dict_two.get(x[3])
            return 7
    if x[0] == 2017:
        return dict_three.get(x[3])


print(main([1997, 'SQL', 1987, 2008, 'YANG']))
print(main([1997, 'J', 1987, 2003, 'EBNF']))
print(main([1997, 'SQL', 1987, 2003, 'EBNF']))
print(main([2017, 'J', 1987, 2008, 'EBNF']))
print(main([1997, 'J', 1987, 1973, 'RUST']))
