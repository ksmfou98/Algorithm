## 백준 2667번 : 단지번호 붙이기

import sys
input = sys.stdin.readline

N = int(input())
aprt = [list(map(int, input().strip())) for _ in range(N)]
arr=[0]*10000
def dfs(x, y, count):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    
    if aprt[x][y] == 1:
        aprt[x][y] = 0
        arr[count] += 1
        dfs(x-1, y, count)
        dfs(x, y-1, count)
        dfs(x+1, y, count)
        dfs(x, y+1, count)
        return True
    return False

result = 0
count = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j, count) == True:
            result += 1
            count += 1

print(result)
dohyun = []
for i in range(count):
    dohyun.append(arr[i])

dohyun.sort(reverse=False)

for i in dohyun:
    print(i)