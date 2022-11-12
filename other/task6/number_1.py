step_one = [1990, 1987, 1980]
step_two = ['JULIA', 'M', 'C', 'KICAD', 'PAN']
step_three = ['ADA', 'HAXE', 'GOSU', 'JULIA', 'M', 'C']
step_four = ['KICAD', 'PAN', 'ADA', 'HAXE', 'GOSU']


def main(x):
    if x[4] == 1990:
        if x[0] == 'JULIA':
            if x[2] == 'ADA':
                return 0
            elif x[2] == 'HAXE':
                if x[1] == 'KICAD':
                    return 1
                elif x[1] == 'PAN':
                    return 2
            elif x[2] == 'GOSU':
                return 3
        elif x[0] == 'M':
            return 4
        elif x[0] == 'C':
            return 5
    elif x[4] == 1987:
        if x[1] == 'KICAD':
            if x[0] == 'JULIA':
                if x[2] == 'ADA':
                    return 6
                elif x[2] == 'HAXE':
                    return 7
                elif x[2] == 'GOSU':
                    return 8
            elif x[0] == 'M':
                return 9
            elif x[0] == 'C':
                return 10
        elif x[1] == 'PAN':
            return 11
    elif x[4] == 1980:
        return 12


print(main(['M', 'KICAD', 'ADA', 1959, 1990]))
print(main(['M', 'KICAD', 'HAXE', 1959, 1987]))
print(main(['M', 'PAN', 'GOSU', 1961, 1987]))
