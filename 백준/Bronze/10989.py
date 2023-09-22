# import sys

# n = int(sys.stdin.readline())
# num_list = []

# for _ in range(n):
#     num_list.append(int(sys.stdin.readline()))

# sorted_list = sorted(num_list)

# for i in sorted_list:
#     print(i)
# 메모리 초과

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
