n, m = list(map(int, input().split(' ')))

x, y, direction = list(map(int, input().split(' ')))

result = 1
map_list = []

for _ in range(m):
    map_list.append(list(map(int, input().split(' '))))

direction_map = {
    0: (0, -1),
    1: (1, 0 ),
    2: (0, 1),
    3: (-1, 0),
}

def next_direction(direction: int) -> int:
    direction -= 1

    if direction == -1:
        direction = 3

    return direction 

while True:
    stop = True

    for _ in range(4):
        new_x = x + direction_map[direction][0]
        new_y = y + direction_map[direction][1]

        if map_list[new_x][new_y] == 0:
            stop = False
            break
        
        direction = next_direction(direction)
    
    if stop:
        break

    map_list[x][y] = 1
    result += 1
    x = new_x
    y = new_y

print(result)