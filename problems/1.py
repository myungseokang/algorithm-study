N = int(input())

characters = list(map(int, input().split()))

characters.sort()

result = 0

tmp = []
for c in characters:
    tmp.append(c)

    if len(tmp) == c:
        tmp = []
        result += 1

print(result)
