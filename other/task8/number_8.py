import re


def main(source):
    pattern = r'#([0-9-]*)->([a-z_0-9]*)\.'
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[1]] = int(news[0])
    return i


print(main("""
do equ#8982 ->legeat. equ#5890 -> gequ_900. end
"""))
