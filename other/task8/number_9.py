import re


def main(source):
    pattern = r'\[glob([a-z_0-9]*)to\"([a-z_0-9]*)\"\]'
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[1]] = news[0]
    return i


print(main("""
\egin[[ glob laon_607 to "lariin"]],[[ glob reat to
"arrila_876"]],[[ glob ratear to"eddiis_842" ]], [[ glob bele_153 to
"argeed" ]], \end
"""))