#################백준 20362번 유니대전 퀴즈쇼##################

import sys
input = sys.stdin.readline

N, S = input().split()

a = []
k = 0
count = 0

for i in range(int(N)):
    first, second = map(str,input().split())
    a.append([first, second])
    if a[i][0] == S:
        k = i

for i in range(k):
    if a[i][1] == a[k][1]:
        count += 1

print(count)
