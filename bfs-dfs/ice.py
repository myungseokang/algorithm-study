N, M = list(map(int, input().split(' ')))

map_list = []
result = 0

for _ in range(N):
    map_list.append(list(map(int, input().split(' '))))


def fill_water(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return

    if map_list[i][j] == 0:
        map_list[i][j] = 1

        fill_water(i - 1, j)
        fill_water(i + 1, j)
        fill_water(i, j - 1)
        fill_water(i, j + 1)

        return True

    return False

for i in range(N):
    for j in range(M):
        if fill_water(i, j) == True:
            result += 1

print(result)
