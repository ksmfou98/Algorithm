### 백준 3009번 네 번째 점 ###

import sys
input = sys.stdin.readline

x = [0]*1001
y = [0]*1001
a = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    x[a[i][0]] += 1
    y[a[i][1]] += 1

for i in range(1001):
    if x[i] == 1:
        print(i, end=" ")


for i in range(1001):        
    if y[i] == 1:
        print(i)
