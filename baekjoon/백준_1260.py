#### 백준 1260번 DFS와 BFS ####

import sys
input = sys.stdin.readline
from collections import deque


N, M, V = map(int, input().split())


b = [[0] * (N+1) for i in range(N+1)]
visit = [0] * (N+1)


for i in range(M):
    x, y = map(int, input().split())
    b[x][y] = 1
    b[y][x] = 1

def dfs(V):
    visit[V] = 1  # 방문했을 때 1로 바꿈
    print(V, end=' ')
    for i in range(1, N+1):
        if b[V][i] == 1 and visit[i] == 0:
            dfs(i)



def bfs(V):
    queue = [V]
    visit[V] = 0   # dfs에서 1로 바꿨으니 여기선 방문하면 0 으로 바꿈
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit[i] == 1 and b[V][i] == 1):
                queue.append(i)
                visit[i] = 0



dfs(V)
print(end="\n")
bfs(V)