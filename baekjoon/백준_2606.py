## 백준 2606번 : 바이러스

import sys
input = sys.stdin.readline


computer = int(input())
network = int(input())

arr = []
real_arr=[]
for i in range(network):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in range(computer+1):
    real_arr.append([])

for x,y in arr:
    real_arr[x].append(y)
    real_arr[y].append(x)

visited = [False] * (computer+1)
count = -1

def dfs(real_arr, v, visited):
    visited[v] = True
    for i in real_arr[v]:
        if not visited[i]:
            dfs(real_arr, i, visited)


dfs(real_arr, 1, visited)

for i in visited:
    if i == 1:
        count += 1
print(count)