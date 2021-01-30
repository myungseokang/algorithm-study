s = input()

result = int(s[0])

for char in s[1:]:
    data = int(char)
    if 0 <= data <= 1 or 0 <= result <= 1:
        result += data
    else:
        result *= data

print(result)
