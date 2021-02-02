#### 백준 2751번 수 정렬하기 2 ####

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    a = int(input())
    arr.append(a)

arr.sort()

for i in arr:
    print(i)