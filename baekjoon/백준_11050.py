##백준 : 11050번 : 이항 계수 1

import sys
input = sys.stdin.readline


N, K = map(int, input().split())  # 이항계수 : nCk

top_result = 1
for i in range(K):
    top_result = top_result * N
    N -= 1

bottom_result = 1
for i in range(K, 0, -1):
    bottom_result = bottom_result * i

print(top_result // bottom_result)



#math.factorial 활용하면
# from math import factorial

# N, K = list(map(int, input().split()))

# print(factorial(N)//(factorial(K) * factorial(N-K)))
