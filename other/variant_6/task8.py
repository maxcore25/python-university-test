import re


def main(source):
    pattern = r'\'([a-z_0-9]*)\'list\(([a-z_0-9\.]*)\)'
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[0]] = news[1].replace('.', ',').split(',')
    return i


print(main("""
[[ <% decl 'reveti' list( xeon_926 . intiso_254 . laar ). %> <% decl
'esus' list( areser . onxe . gedi_41). %> <% decl 'race' list( oron .
soarxe . cein_201 . atin ). %> ]]
"""))

