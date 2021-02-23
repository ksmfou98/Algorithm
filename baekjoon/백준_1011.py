## 백준 1011번 : Fly me to the Alpha Centauri

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    cnt = 0
    vin = 1
    result = 0

    while result < d:
        cnt += 1
        result += vin
        if cnt % 2 == 0:
            vin += 1
    print(cnt)
