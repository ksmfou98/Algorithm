## 백준 1697번 : 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
queue.append([N, 0])
visited = [0] * 100001

while queue:
    p, d = queue[0][0], queue[0][1]
    if p == K:
        break
    queue.popleft()
    visited[p] = 1

    if p - 1 > 0 and visited[p - 1] == 0:
        queue.append([p - 1, d + 1])
    if p + 1 < 100001 and visited[p + 1] == 0:
        queue.append([p + 1, d + 1])
    if p * 2 < 100001 and visited[p * 2] == 0:
        queue.append([p * 2, d + 1])


print(queue[0][1])