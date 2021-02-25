## 백준 9020번 : 골드바흐의 추측

import sys
import math
input = sys.stdin.readline


T = int(input())  #테스트 케이스


def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return 1

arr = []
for j in range(10011):
        if isPrime(j) == 1:
            arr.append(j)



    
for i in range(T):
    n = int(input())  # 짝수

    for j in range(len(arr)):
        item = n-arr[j]
        if isPrime(item) == 1 and arr[j] <= item:
            k = arr[j]
            t = item
        if arr[j] > item:
            break
        else:
            continue

    print(k, t)



# import sys
# MAX = 10000
# eratos = [False] * 2 + [True] * (MAX - 1)

# for i in range(int(MAX ** 0.5) + 1):
#   if eratos[i]:
#     for j in range(i * 2, MAX + 1, i):
#       eratos[j] = False

# def get_partition(n):
#   pair1, pair2 = 0, 0
#   for i in range(n // 2, -1, -1):
#     pair = n - i
#     if eratos[i] and eratos[pair]:
#       pair1, pair2 = min(i, pair), max(i, pair)
#       break
  
#   return f'{pair1} {pair2}'

# n = int(sys.stdin.readline().strip())
# for _ in range(n):
#   print(get_partition(int(sys.stdin.readline().strip())))