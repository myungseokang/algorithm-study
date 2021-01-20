N = int(input())

character = [1, 1]
move_plan = input().split(' ')

for plan in move_plan:
    if plan == 'R' and character[0] + 1 <= N:
        character[0] += 1
    elif plan == 'L' and character[0] - 1 >= N:
        character[0] -= 1
    elif plan == 'U' and character[1] - 1 >= N:
        character[1] -= 1
    elif plan == 'D' and character[1] + 1 <= N:
        character[1] += 1

print(f"{character[0]} {character[1]}")
