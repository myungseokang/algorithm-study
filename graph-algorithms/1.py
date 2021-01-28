N, M = list(map(int, input().split()))

parents = [n for n in range(N + 1)]

road_list = [list(map(int, input().split())) for _ in range(M)]

def find_parent(x):
    global parents

    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    
    return x


def union_elements(a, b):
    global parents

    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for road in road_list:
    operation, a, b = road

    if operation == 0:
        union_elements(a, b)
    elif operation == 1:
        # 루트 노드가 같은 경우
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
