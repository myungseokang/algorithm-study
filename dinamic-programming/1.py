from collections import defaultdict

N = int(input())

calc_map = defaultdict(int)

for i in range(2, N + 1):
    idx = i - 1

    calc_map[i] = calc_map[idx] + 1

    if i % 2 == 0:
        calc_map[i] = min(calc_map[i], calc_map[idx // 5] + 1)

    if i % 3 == 0:
        calc_map[i] = min(calc_map[i], calc_map[idx // 3] + 1)

    if i % 5 == 0:
        calc_map[i] = min(calc_map[i], calc_map[idx // 2] + 1)

print(calc_map)
print(calc_map[N])
