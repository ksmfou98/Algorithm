######### 10845번 큐 ############

import sys
input = sys.stdin.readline

N = int(input())
queue = []

def queue_push(X):
    queue.append(X)
    return queue

def queue_pop():
    if len(queue) == 0:
        print(-1)
    else :
        print(queue[0])
        del queue[0]
    return queue

def queue_size():
    print(len(queue))

    return queue

def queue_empty():
    if len(queue) == 0:
        print(1)

    else :
        print(0)
    return queue

def queue_front():
    if len(queue) == 0:
        print(-1)

    else :
        print(queue[0])
    return queue

def queue_back():
    if len(queue) == 0:
        print(-1)

    else:
        print(queue[len(queue)-1])

    return queue



for i in range(N):
    a = list(map(str, input().split()))

    if a[0] == 'push':
        queue_push(a[1])
    
    elif a[0] == 'pop':
        queue_pop()

    elif a[0] == 'size':
        queue_size()

    elif a[0] == 'empty':
        queue_empty()

    elif a[0] == 'front':
        queue_front()
    
    elif a[0] == 'back':
        queue_back()