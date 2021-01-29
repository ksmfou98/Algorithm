#################백준 1149번 RGB 거리 ###################

import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(len(arr)-1):
    arr[i+1][0] += min(arr[i][1], arr[i][2])
    arr[i+1][1] += min(arr[i][0], arr[i][2]) 
    arr[i+1][2] += min(arr[i][0], arr[i][1])

T = len(arr)-1
print(min(arr[T][0], arr[T][1], arr[T][2]))