N = input()

num_sum = 0
data = []

for n in N:
    if n.isdigit():
        num_sum += int(n)
    else:
        data.append(n)

print(f"{''.join(sorted(data))}{num_sum}")
