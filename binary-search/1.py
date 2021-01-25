import sys

N = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))

M = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def search(target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if n_list[mid] == target:
        return True

    if target < n_list[mid]:
        return search(target, start, mid - 1)
    else:
        return search(target, mid + 1, end)

n_list.sort()

for m in m_list:
    if search(m, 0, len(n_list) - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
