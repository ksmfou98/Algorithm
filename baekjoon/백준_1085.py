### 백준 1085번 직사각형에서 탈출 ###

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

a = 0
b = 0

if w-x > x-0:
    a = x
else :
    a = w-x

if h-y > y-0:
    b = y
else:
    b = h-y

if a > b:
    print(b)

else:
    print(a)