N = input()

# 중간 인덱스
mid = (len(N) // 2)

left_sum = sum([int(N[i]) for i in range(0, mid)])
right_sum = sum([int(N[i]) for i in range(mid, len(N))])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
