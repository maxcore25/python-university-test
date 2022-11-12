import re


def main(source):
    pattern = r'#([0-9-]*)==>\s*@\'([a-z_0-9]*)\'\.'
    i = {}
    sr = source.replace(" ", "").replace("\n", "")
    new = re.findall(pattern, sr)
    for news in new:
        i[news[1]] = int(news[0])
    return i


print(main("""
<sect> do val #-5471==> @'enus_231'. od;do val #-2638 ==>
@'rian_496'. od;do val #-6055==>@'erisra'. od;</sect>
"""))
