import re


def main(source):
    pattern = r'q\(([a-z_0-9]*)\)is\'([a-z_0-9]*)\''
    i = {}
    sr = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, sr)
    for news in new:
        i[news[0]] = news[1]
    return i


print(main("""
.begin(( auto q(bebila_128) is'edxe' ))((auto q(laesen)is
'ondiso_83'))(( auto q(lequma_893)is'sove_981' )) .end
"""))