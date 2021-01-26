from collections import defaultdict

N = int(input())

snack_list = list(map(int, input().split(' ')))

calc_map = defaultdict(int)

calc_map[0] = snack_list[0]
calc_map[1] = max(snack_list[0], snack_list[1])

for i in range(2, N):
    calc_map[i] = max(calc_map[i - 1], calc_map[i - 2] + snack_list[i])

print(calc_map[N - 1])
