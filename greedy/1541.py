import re

equation = input()

data_list = []
tmp = ''
for idx, character in enumerate(equation):
    if character in ('-', '+'):
        data.append(character)
    elif character and equation[idx + 1]:
        tmp += character
        data_list.append(int(tmp))
    elif character:
        tmp += character
