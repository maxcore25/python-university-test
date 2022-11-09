import re


def main(src):
    pattern = r'@\'(\w*)\'<==#(-?[0-9]*)'
    src = src.replace(' ', '').replace('\n', '')
    matches = re.findall(pattern, src)
    my_dict = {}

    for match in matches:
        my_dict[match[0]] = int(match[1])

    return my_dict


print(main('''
|| let @'entier_710' <==#397. ||. || let @'xetien'<== #-3374.||. ||
let @'diqu_178' <==#-2508.||.|| let @'diquis_323' <== #-2632. ||
'''))
print(main('''
|| let @'lexe_979' <==#-6280. ||. ||let @'atmaen'<== #2791. ||.||let
@'birema_798' <== #-2216. ||.
'''))
