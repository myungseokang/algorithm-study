location = input()

x = int(ord(location[0]) - 96)
y = int(location[1])

result = 1

move_list = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, 1),
    (2, -1),
    (1, 2),
    (-1, 2),
)
result = 0

for move in move_list:
    if 1 <= x + move[0] <= 8 and 1 <= y + move[1] <= 8:
        result += 1

print(result)
