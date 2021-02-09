### 백준 1904번 01타일 ###

import sys
input = sys.stdin.readline

N = int(input())

arr = [0, 1, 2]

if N >= 3:
    for i in range(3, N+1):
        a = (arr[i-1] + arr[i-2]) % 15746
        arr.append(a)

print(arr[N])




