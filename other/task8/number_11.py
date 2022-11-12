import re


def main(source):
    pattern = r'auto([a-z_0-9]*)<=\[([a-z_0-9\.]*)\]'
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[0]] = news[1].replace(".", ",").split(",")
    return i


print(main("""
| || auto usmaxe <= [onso_882 . abiinis_643 . anxe];||, ||auto maedla
<= [anre . anus . eses_805 ];||,|| auto tibebi_499 <= [ erri . usedle
]; ||, || auto usinus <= [bema . main_509 . orer]; ||,|
"""))
