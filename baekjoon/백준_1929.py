## 백준 1929번 : 소수 구하기


import sys
import math
input = sys.stdin.readline
M, N = map(int, input().split())

for i in range(M, N+1):
    result = 0
    for j in range(1, int(math.sqrt(i)) + 1):  # 어떤 수 N이 소수인지 판별하려면 2~루트N 까지 나눠봐서 개수가 0개이면 소수이다.
        if i % j == 0:
            result += 1
            if result > 1:
                break
        
    if result == 1 and i != 1:
        print(i)
