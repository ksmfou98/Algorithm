#################백준 13305번 주유소 ###################

import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수

road = list(map(int, input().split())) #도로의 거리

cost = list(map(int, input().split())) #왼쪽 도로부터 리터당 가격

result = 0
m = cost[0]

for i in range(N-1):
    if m > cost[i]:
        m = cost[i]
    result = result + (m * road[i])


    

print(result)