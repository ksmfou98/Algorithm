#################백준 7568번 덩치 ###################

import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
result = []
for i in range(N):
    count = 0
    for j in range(N):
        if (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]):
            count += 1
    result.append(count+1)

for i in result:
    print(i, end=" ")