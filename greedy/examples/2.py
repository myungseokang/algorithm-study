N, M, K = input().split(' ')
num_list = input().split(' ')

N = int(N)
M = int(M)
K = int(K)
num_list = [int(n) for n in num_list]

first_max = max(num_list)
num_list.remove(first_max)

second_max = max(num_list)

cnt = K
result = first_max * K
is_first = False

while cnt < M:
    if is_first:
        result += first_max
        cnt += 1
        if cnt % K == 0:
            is_first = False
    else:
        result += second_max
        cnt += 1
        is_first = True

print(result)
