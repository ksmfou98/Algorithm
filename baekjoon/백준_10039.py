#### 백준 10039번 평균 점수 ###

import sys
input = sys.stdin.readline


result = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    result += a

print(result//5)
