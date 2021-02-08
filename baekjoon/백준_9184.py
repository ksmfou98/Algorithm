### 백준 9184번 신나는 함수 실행 ###

import sys
input = sys.stdin.readline

result = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def dohyun(a, b, c):

    if a<=0 or b<=0 or c<=0:        
        return 1     
        
    if a>20 or b>20 or c>20:
        return dohyun(20,20,20)
 

    if result[a][b][c] != 0:
        return result[a][b][c]

    
    if a<b and b<c:
        result[a][b][c] = dohyun(a, b, c-1) + dohyun(a, b-1, c-1) - dohyun(a, b-1, c)
        return result[a][b][c]
       
    else :
        result[a][b][c] = dohyun(a-1, b, c) + dohyun(a-1, b-1, c) + dohyun(a-1, b, c-1) - dohyun(a-1, b-1, c-1)
        return result[a][b][c]


while 1:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print("w({}, {}, {}) = {}".format(x, y, z, dohyun(x, y, z)))

    
    



