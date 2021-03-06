## 백준 10870번 피보나치 수 5

import sys
input = sys.stdin.readline

pibo = [0]*21
pibo[0] = 0
pibo[1] = 1

n = int(input())

for i in range(2, n+1):
    pibo[i] = pibo[i-1] + pibo[i-2]

print(pibo[n])