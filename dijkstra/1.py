import heapq

INF = int(1e9)

N, M = list(map(int, input().split()))

graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

# 자기 자신으로 가는 건 노코스트
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 간선 데이터
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = list(map(int, input().split()))

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


to_k_dist = graph[1][K]
k_to_x_dist = graph[K][X]

if to_k_dist != INF and k_to_x_dist != INF:
    print(to_k_dist + k_to_x_dist)
else:
    print(-1)
