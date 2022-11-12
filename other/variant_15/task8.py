import re


def main(source):
    pattern = r'do([a-z_0-9]*)<=([a-z_0-9]*);'
    i = {}
    placeremover = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, placeremover)
    for news in new:
        i[news[0]] = news[1]
    return i


print(main("""
<: do riar <= tianat; end; do enrius <=qureso; end; do ries_982
<=riri_974; end;:>
"""))