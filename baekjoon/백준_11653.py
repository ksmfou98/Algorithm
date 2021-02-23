## 백준 11653번 : 소인수 분해

import sys
input = sys.stdin.readline

N = int(input())

k = 2
while 1:
    if N % k == 0:
        print(k)
        N = N // k
        k = 1

    if N == 1:
        break
    k += 1
