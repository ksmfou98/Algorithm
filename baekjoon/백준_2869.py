## 백준 2869번 : 달팽이는 올라가고 싶다

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day = (V-A) // (A-B)  # 날

if (V-A) % (A-B) == 0:
    print(day+1)
else:
    print(day+2)