## 백준 9095번 : 1, 2, 3 더하기

import sys
input = sys.stdin.readline

T = int(input())  # test case
arr = [0]*11
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(T):
    n = int(input())

    if n > 3:
        for j in range(4, n+1):
            arr[j] = arr[j-1] + arr[j-2] + arr[j-3]
    print(arr[n])
        


