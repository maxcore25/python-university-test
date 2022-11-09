import re


def main(source):
    pattern = r'{(((-?\d*);?)*)}to(\w*)'
    my_dict = {}
    space_removed = source.replace(" ", "").replace("\n", "")
    matches = re.findall(pattern, space_removed)
    for match_list in matches:
        arr = match_list[0].split(';')
        int_arr = []
        for i in arr:
            int_arr.append(int(i))
        my_dict[match_list[-1]] = int_arr
    return my_dict


print(main("""
<block> << glob { 3189 ; -3209 ; -5950}to diin_253; >>.<< glob{ -7444
; -8902} to lebera; >>.<< glob{ 5540 ; 9528 ;1629 }to leate; >>.
</block>
"""))
