N, M = list(map(int, input().split()))

ball_data = list(map(int, input().split()))

count = 0
for first_idx, first_val in enumerate(ball_data):
    for second_idx, second_val in enumerate(ball_data[first_idx:]):
        if first_val != second_val:
            count += 1

print(count)
