s = input()

data_map = {
    0: 0,
    1: 0,
}

tmp = int(s[0])
data_map[tmp] += 1

for character in s[1:]:
    data = int(character)
    if tmp != data:
        data_map[data] += 1

    tmp = data


print(sorted([i for i in data_map.values()])[0])
