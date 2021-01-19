coin_count, amount = map(int, input().split(' '))

coins = []

for _ in range(coin_count):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
cnt = 0

for coin in coins:
    if coin > amount:
        continue
    
    cnt += amount // coin
    amount %= coin   

print(cnt)
