dict1 = {'VUE': 0, 'MESON': 1, }
dict2 = {'SCSS': 2, 'FISH': 3, }
dict3 = {'VUE': 4, 'MESON': 5, }
dict4 = {'VUE': 6, 'MESON': 7, }
dict5 = {'MUPAD': 9, 'SCSS': 10, 'FISH': 11}


def main(x):
    if x[3] == 1964:
        if x[0] == 'MUPAD':
            return dict1[x[1]]
        return dict2[x[0]]
    elif x[3] == 2004:
        if x[0] == 'MUPAD':
            return dict3[x[1]]
        if x[0] == 'SCSS':
            return dict4[x[1]]
        return 8
    elif x[3] == 2002:
        if x[1] == 'VUE':
            return dict5[x[0]]
        return 12


print(main(['FISH', 'MESON', 'REXX', 2002]))
print(main(['MUPAD', 'MESON', 'REXX', 1964]))
print(main(['SCSS', 'VUE', 'ALLOY', 2002]))
print(main(['SCSS', 'MESON', 'REXX', 2004]))
print(main(['MUPAD', 'VUE', 'REXX', 1964]))
