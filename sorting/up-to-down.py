N = int(input())

data_list = []

for _ in range(N):
    data_list.append(int(input()))

print(" ".join(sorted(data_list, reverse=True)))
