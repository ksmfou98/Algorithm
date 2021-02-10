### 백준 1463번 1로 만들기 ###

import sys
input = sys.stdin.readline




N = int(input())


T = N + 3
arr = [0]*T
arr[1] = 0
arr[2] = 1
arr[3] = 1

if N > 3:
    for i in range(4, N+1):
        if i % 2 == 0 and i % 3 != 0:
            arr[i] = min((arr[i//2]+1), arr[i-1]+1)
        elif i % 3 == 0 and i % 2 != 0:
            arr[i] = min((arr[i//3]+1), arr[i-1]+1)
        elif i % 2 ==0 and i % 3 == 0:
            arr[i] = min((arr[i//2]+1), (arr[i//3]+1), (arr[i-1]+1))
        else:
            arr[i] = arr[i-1] + 1

print(arr[N])

