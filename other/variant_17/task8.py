import re


def main(source):
    pattern = r'variable"([a-z_0-9]*)"to`([a-z_0-9]*);'
    i = {}
    placeremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, placeremove)
    for news in new:
        i[news[1]] = news[0]
    return i


print(main("""
<block> variable "bege_330"to `soatce; variable "geen_73"to `anve;
</block>
"""))
