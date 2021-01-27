#################백준 1193번 분수 찾기 ###################

import sys
input = sys.stdin.readline

N = int(input())
k = 1
s = 1
x = 1
y = 1
for i in range(1, N+2):
    if N == 1:
        break
    if N >= k:
        k = k + i
        continue
    else:
        k = k - (i-1)
        s = i - 1
        break

k = N - k + 1

if s % 2 == 1:
    y = k
    x = s - k + 1
else:
    y = s - k + 1
    x = k


print('{}/{}'.format(x,y))