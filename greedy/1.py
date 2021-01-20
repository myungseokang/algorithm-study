money = int(input())

result = {
    500: 0,
    100: 0,
    50: 0,
    10: 0,
}

for amount in result.keys():
    cnt = money // int(amount)
    result[amount] += cnt
    money = money % amount

print(result)
