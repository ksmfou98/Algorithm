#################백준 11721번 열 개씩 끊어 출력하기 ###################

import sys
input = sys.stdin.readline

N = input()

b = 10

for i in range(0,len(N),10):
    print(N[i:b])
    b += 10