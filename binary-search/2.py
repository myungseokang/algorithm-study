import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))

data_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
data_list.sort()
result = []

def calc_height(value):
    global data_list
    tmp = [data for data in data_list if data > value]
    return sum(tmp) - (len(tmp) * value)

def search(target, start, end):
    global data_list
    global result

    if start > end:
        return 0
    
    mid = (start + end) // 2
    val = calc_height(mid)
    if val >= target:
        result.append(mid)
        return search(target, mid + 1, end)
    else:
        return search(target, start, mid - 1)

search(M, 0, max(data_list))
print(sorted(result, reverse=True)[0])
