### 백준 9461번 파도반 수열 ###

import sys
input = sys.stdin.readline


T = int(input())



for i in range(T):
    P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    N = int(input())
    if N <= 10:
        print(P[N])
    else:
        for j in range(11, N+1):
            a = P[j-5] + P[j-1]
            P.append(a)
        print(P[N])




