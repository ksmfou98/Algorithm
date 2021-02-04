######### 10828번 스택 ############

import sys
input = sys.stdin.readline


N = int(input())
stack = []

def stack_push(X):
    stack.append(X)
    return stack

def stack_pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])
        stack.pop()

    return stack

def stack_size():
    print(len(stack))
    return stack

def stack_empty():
    if len(stack) == 0 :
        print(1)
    else :
        print(0)

    return stack

def stack_top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])

    return stack
for i in range(N):
    a = list(map(str, input().split()))
    if a[0] == 'push':
        stack_push(a[1])
    
    elif a[0] == 'pop':
        stack_pop()

    elif a[0] == 'size':
        stack_size()

    elif a[0] == 'empty':
        stack_empty()

    elif a[0] == 'top':
        stack_top()