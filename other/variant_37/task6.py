dict_one = {2000: 0, 2002: 1, 2012: 2}
dict_two = {'CSON': 5, 'POD': 6, 'PAN': 7}
dict_three = {2000: 8, 2002: 9, 2012: 10}


def main(x):
    if x[0] == 2011:
        if x[2] == 'CSON':
            return dict_one.get(x[1])
        elif x[2] == 'POD':
            return 3
        elif x[2] == 'PAN':
            return 4
    elif x[0] == 2015:
        return dict_two.get(x[2])
    elif x[0] == 2017:
        return dict_three.get(x[1])


print(main([2015, 2000, 'POD', 2018]))
print(main([2017, 2012, 'CSON', 1974]))
print(main([2011, 2002, 'POD', 1974]))
print(main([2017, 2000, 'POD', 1974]))
print(main([2015, 2012, 'PAN', 1974]))
