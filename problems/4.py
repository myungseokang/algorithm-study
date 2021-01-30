N = int(input())

coins = list(map(int, input().split()))

coins.sort(reverse=True)

result = 1

while True:
    if result in coins:
        result += 1
        continue

    tmp = result
    for coin in coins:
        if tmp == 0:
            break

        if tmp < coin:
            continue
        
        tmp -= coin

        if tmp == 0:
            break

    if tmp == 0:
        result += 1
    else:
        break


print(result)
