N = int(input())

result = 0

for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            a = f"{hour}{minute}{second}"
            if str(N) in a:
                result += 1

print(result)
