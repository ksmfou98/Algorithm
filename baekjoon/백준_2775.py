## 백준 2775번 : 부녀회장이 될테야

import sys
input = sys.stdin.readline

T = int(input())



for i in range(T):
    
    k = int(input())
    n = int(input())

    a = [[0 for i in range(15)] for j in range(k+1)]
    for i in range(15):
        a[0][i] = i

    for j in range(1, k+1):
        for s in range(1, n+1):
            a[j][s] = a[j][s-1] + a[j-1][s]

    print(a[k][n])
