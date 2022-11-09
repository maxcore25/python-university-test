import re


def main(src):
    pattern = r'set(\w*)\|>@"(\w*)"'
    src = src.replace(' ', '').replace('\n', '')
    my_dict = {}
    matches = re.findall(pattern, src)

    for match in matches:
        my_dict[match[1]] = match[0]

    return my_dict


print(main('''
<sect> [set titeen_947 |>@"edaso" ]. [ set inti |> @"anre"].[ set ques
|> @"atle" ]. [ set atxe |> @"quxe_168" ].</sect>
'''))
print(main('''
<sect> [ set recere_906 |>@"tidien"].[ set gemadi_34|>@"esti_834"
].</sect>
'''))
