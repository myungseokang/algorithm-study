n = int(input())

conference_list = []

for _ in range(n + 1):
    start, end = map(int, input().split(' '))
    conference_list.append((start, end))


