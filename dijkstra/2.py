import heapq

INF = int(1e9)

N, M, C = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

# 간선 데이터
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now_node = heapq.heappop(q)

        # 현재 거리보다 클 경우 무시하기
        if distance[now_node] < dist:
            continue

        # 인접 노드들 가져와서 거리에 따라 큐에 넣기
        for i in graph[now_node]:
            new_dist = dist + i[1]
            # 새로운 거리가 인접한 노드의 기존 거리보다 작은 경우에는 해당 노드의 거리를 바까버리고, 큐에 넣음
            if new_dist < distance[i[0]]:
                distance[i[0]] = new_dist
                heapq.heappush(q, (new_dist, i[0]))

dijkstra(C)

total_time = 0
city_count = 0
for dist in distance:
    # 못 가는 곳이랑 자기 자신 제외
    if dist != INF and dist != 0:
        city_count += 1
        total_time += dist


print(distance)
print(city_count, total_time)