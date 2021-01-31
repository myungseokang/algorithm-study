import copy

N = int(input())

K = int(input())

map_data = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    x, y = list(map(int, input().split()))
    map_data[x - 1][y - 1] = 1

L = int(input())

turn_map = {}
for _ in range(L):
    t, d = input().split()
    turn_map[t] = d

direction_map = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}

def turn_right(d):
    return (d + 1) % 4
    
def turn_left(d):
    new_d = (d - 1)
    return 3 if new_d < 0 else new_d

now_direction = 0

snake = [
    [0, 0],
]
t = 0

while True:
    t += 1

    origin_tail = [0, 0]
    origin_head = [0, 0]
    origin_head[0] = snake[0][0]
    origin_head[1] = snake[0][1]

    # 머리의 다음 좌표가 맵밖인지 확인
    dx, dy = direction_map[now_direction]
    new_head_x = origin_head[0] + dx
    new_head_y = origin_head[1] + dy

    if not (0 <= new_head_x < N) or not (0 <= new_head_y < N):
        break

    # 이동
    for idx in range(1, len(snake)):
        if idx == len(snake) - 1:
            origin_tail[0] = snake[-1][0]
            origin_tail[1] = snake[-1][1]

        snake[idx][0] = snake[idx - 1][0]
        snake[idx][1] = snake[idx - 1][1]

    snake[0] = [new_head_x, new_head_y]

    for a in snake:
        for b in snake:
            if a == b:
                break

    # 사과 먹었는지 확인
    if map_data[new_head_x][new_head_y] == 1:
        snake.append([origin_tail[0], origin_tail[1])
        map_data[new_head_x][new_head_y] == 0

    # 회전해야되는지 확인
    if str(t) in turn_map:
        if turn_map[str(t)] == 'L':
            now_direction = turn_left(now_direction)
        elif turn_map[str(t)] == 'D':
            now_direction = turn_right(now_direction)

    print(t, snake)

print(t)
