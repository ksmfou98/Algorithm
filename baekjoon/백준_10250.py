#################백준 10250번 ACM 호텔 ###################

import sys
input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    H, W, N = map(int, input().split())
    dohyun = N
    count = 1
    while(dohyun > H):
        dohyun = dohyun - H
        count += 1
    
    result.append(dohyun*100+count)


for i in range(len(result)):
    print(result[i], end="\n")


