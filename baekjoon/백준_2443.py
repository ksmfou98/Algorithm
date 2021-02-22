## 백준 2443번 : 별 찍기 -6

import sys
input = sys.stdin.readline

N = int(input())


k = 0
for i in range(N-1, -1, -1):
    print(" " * k + "*" * (2*i+1))
    k += 1

