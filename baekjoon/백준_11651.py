## 백준 11651번 : 좌표 정렬하기 2

import sys

input = sys.stdin.readline

N = int(input())
graph = []

for i in range(N):
    x, y = map(int, input().split())
    graph.append([x, y])
graph.sort(key=lambda x: (x[1], x[0]))

for i in graph:
    print(i[0], i[1])