import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([])

for i in range(N):
    arr = input().split()
    if arr[0] == 'push':
        queue.append(int(arr[1]))

    elif arr[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif arr[0] == 'size':
        print(len(queue))

    elif arr[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif arr[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif arr[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])

