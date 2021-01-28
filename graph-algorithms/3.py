from collections import deque
import copy

N = int(input())

진입차수 = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
time_list = [0 for _ in range(N + 1)]
road_list = []
result = 0

for n in range(1, N + 1):
    data = list(map(int, input().split()))
    time_list[n] = data[0]

    for i in data[1:-1]:
        진입차수[n] += 1
        graph[i].append(n)


def tp_sort():
    result = copy.deepcopy(time_list)
    q = deque()

    for node in range(1, n + 1):
        if 진입차수[node] == 0:
            q.append(node)
    
    while q:
        now_node = q.popleft()

        for i in graph[now_node]:
            result[i] = max(result[i], result[now_node] + time_list[i])
            진입차수[i] -= 1
            if 진입차수[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])


tp_sort()
