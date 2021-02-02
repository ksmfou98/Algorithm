#### 백준 1427번 소트인사이드 ####

import sys
input = sys.stdin.readline


N = int(input())

arr = []

while N != 0:
    arr.append(N % 10)
    N = N // 10

arr.sort(reverse=True)
for i in arr:
    print(i, end="")