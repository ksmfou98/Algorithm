#################백준 2441번 별 찍기-4 ###################

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for j in range(0, i):
        print(end=" ")

    for k in range(N, i, -1):
        print("*", end="")

    print(end="\n")

