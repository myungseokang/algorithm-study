N, M = map(int, input().split(' '))

num_data = []
min_data = []

for _ in range(N):
    data = map(int, input().split(' '))
    min_data.append(min(data))
    num_data.append(data)

print(max(min_data))
