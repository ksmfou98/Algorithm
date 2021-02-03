#### 백준 11650번 좌표 정렬하기 ####

import sys
input = sys.stdin.readline


N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(reverse=False)
for x, y in arr:
    print(x, end=" ")
    print(y, end="\n")

