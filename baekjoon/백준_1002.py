### 백준 1002번 터렛 ###

import sys
import math    # 루트 계산를 위해서 선언!
input = sys.stdin.readline

T = int(input())  #테스트 케이스의 수

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = 0

    d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))  # 두 점사이의 거리 

    
    maxR = max(r1, r2)   # 두 반지름중 큰 반지름 저장
    minR = min(r1, r2)   # 두 반지름 중 작은 반지름 저장

    # 두 원의 접점 갯수 대로 분류 ( 두점에서 만날 떄, 접할 때, 안만날 때, 똑같을 때)

    if (maxR - minR) < d and d < (maxR + minR):   # 1) 두점에서 만날 때 공식 : r - r` < d  < r + r`
        print(2) 
    
    elif (maxR + minR) == d or ((maxR - minR) == d and (x1 != x2 or y1 != y2)):   # 2) 접할 때 r + r` = d  또는 r - r` = 0 이면서 두 중심이 같지않을때
        print(1)

    elif (x1 == x2) and (y1 == y2) and (r1 == r2):   # 3) 두 원이 같을 때
        print(-1)  
    
    elif (maxR + minR) < d or (maxR - minR) > d:   # 4) 두원이 안만날 때 : r + r` < d  또는 r - r` > d
        print(0)
    
    elif d == 0 and r1 != r2:   # 4) 두원이 안만날 때   : d = 0 이면서 r1 != r2 일 때
        print(0)

    
 #   https://mathbang.net/101  이 블로그에 원이 위치관계에 대해서 자세히 나와있음 