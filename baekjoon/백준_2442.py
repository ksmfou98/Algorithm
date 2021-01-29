#################백준 2442번 별 찍기 -5 ###################

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, 0, -1):
    print(" " * (i-1) + "*" * ((2*N-1) - (i-1)*2))