## 백준 2444번 : 별 찍기 -7

import sys
input = sys.stdin.readline

N = int(input())

for i in range(0, N):
    print(" " * (N-i-1) + "*" * (2*i+1))

k = 1
for i in range(N-2, -1, -1):
    print(" " * k + "*" * (2*i+1))
    k += 1

