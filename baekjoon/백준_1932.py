### 백준 1932번 정수 삼각형 ###

import sys
input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
    a = [0]
    num = list(map(int, input().split()))
    a.extend(num)
    a.append(0)
    arr.append(a)

for i in range(1, N):
    for j in range(1, i+2):
        arr[i][j] = max((arr[i-1][j-1]+arr[i][j]), (arr[i-1][j]+arr[i][j]))

print(max(arr[N-1]))


