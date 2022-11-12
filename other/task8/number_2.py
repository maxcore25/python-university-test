import re


def main(source):
    pattern = r'make([a-z_0-9]*)=([0-9-]*)'
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[0]] = int(news[1])
    return i

print(main("""
<section> make leenxe_887 = -9070 make leor = 2497 make aon=2503 make
cece =-2355</section>
"""
))