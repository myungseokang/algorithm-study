people_count = int(input())
time_list = sorted(list(map(int, input().split(' '))))

result = 0

for idx, time in enumerate(time_list):
    loop_count = people_count - idx
    result += time * loop_count

print(result)
