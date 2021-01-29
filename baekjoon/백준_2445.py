#################백준 2445번 별 찍기 -8 ###################

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print("*" * i + " " * (2*N-(i*2)) + "*"*i)

k = 2
for i in range(N-1, 0, -1):
    print("*" * i + " " * k + "*"*i)
    k += 2