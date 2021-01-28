N, M = list(map(int, input().split()))

parents = [n for n in range(N + 1)]

road_list = [list(map(int, input().split())) for _ in range(M)]
# 3번째가 길 유지비용
road_list = sorted(road_list, key=lambda x: x[2])

def find_parent(x):
    global parents

    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    
    return parents[x]

def union_elements(a, b):
    global parents

    x = find_parent(a)
    y = find_parent(b)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

result = 0
max_fee = 0
for road in road_list:
    fee, a, b = road

    if find_parent(a) != find_parent(b):
        union_elements(a, b)
        result += fee
        max_fee = fee

print(result, max_fee)
print(result - max_fee)
