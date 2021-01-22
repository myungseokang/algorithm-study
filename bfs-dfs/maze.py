N, M = list(map(int, input().split(' ')))

map_list = []
result = 1

for _ in range(N):
    map_list.append(list(map(int, input())))

i, j = 0, 0

while i != (N - 1) or j != (M - 1):
    if i + 1 <= (N - 1) and map_list[i + 1][j] == 1:
        i += 1
        result += 1
    elif j + 1 <= (M - 1) and map_list[i][j + 1] == 1:
        j += 1
        result += 1

print(result)
