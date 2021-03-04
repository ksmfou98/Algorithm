## 백준_2217번 로프

import sys
input = sys.stdin.readline

N = int(input())
arr = []
result = 0
for i in range(N):
    a = int(input())
    arr.append(a)

arr.sort(reverse=True)
for i in range(len(arr)):
    arr[i] = arr[i] * (i+1)
print(max(arr))