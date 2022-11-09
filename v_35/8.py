import re


def main(src):
    pattern = r'val(\w*)<\|"(\w*)"'
    src = src.replace(' ', '').replace('\n', '')
    my_dict = {}
    matches = re.findall(pattern, src)

    for match in matches:
        my_dict[match[0]] = match[1]

    return my_dict


print(main('''
do(val bila_470 <|"ededso" ), (val istila_380<| "vea_810" ),end
'''))
print(main('''
do( val esin <| "soisve_541" ),( val maedma <|"inceri_816" ), ( val
sove <|"mara" ), (val auscebe_142 <|"tiinxe_248" ),end
'''))
