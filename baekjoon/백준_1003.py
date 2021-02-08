### 백준 1003번 피보나치 함수 ###

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
   
    arr = []
    for i in range(n+1):
        arr.append([i, 0, 0])

    
    arr[0][1] = 1

    if n >= 2:
        arr[1][2] = 1
        for i in range(2, n+1):
            arr[i][1] = arr[i-1][1] + arr[i-2][1]  #zero
            arr[i][2] = arr[i-1][2] + arr[i-2][2]  #one
    elif n == 1:
        arr[1][2] = 1
    
    print(arr[n][1], arr[n][2])
        



