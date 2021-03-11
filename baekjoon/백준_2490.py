## 백준 2490번 : 윷놀이

import sys
input = sys.stdin.readline

for i in range(3):
    arr = list(map(int, input().split()))
    count = 0
    for j in arr:
        if j == 0:
            count += 1
    
    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
