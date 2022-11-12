import re


def main(source):
    pattern = r'glob([a-z_0-9]*)<==\{([0-9-;]*)\}'
    i = {}
    spaceremove = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, spaceremove)
    for news in new:
        i[news[0]] = news[1].replace(";", ",").split(",")
    return i


print(main("""
<block> <: glob arra <== {7080 ; 161 ;5451 ; -3337 }.:>,<: glob
esleri_841<== { 1274; -6585 ;-151 ;7235 }.:>, <: glob edquti <=={ 5959
;-1302 }. :>,<: glob sore<== { 3773 ; 1680; 2132 ;-8860}. :>, </block>
"""))
