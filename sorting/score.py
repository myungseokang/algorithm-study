N = int(input())

data_list = []

for _ in range(N):
    name, score = input().split(' ')

    data_list.append((name, int(score)))

data_list = sorted(data_list, key=lambda x: x[1])

for data in data_list:
    print(data[0], end=' ')
