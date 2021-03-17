## 백준 1012번 : 유기농 배추

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


for i in range(T):
    M, N, K = map(int, input().split())

    arr = [[0 for o in range(N)] for p in range(M)]

    for d in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1

    result = 0
    for u in range(M):
        for q in range(N):
            if dfs(u, q) == True:
                
                result += 1
                

    print(result)

    