#################백준 2750번 수 정렬하기##################

import sys
input = sys.stdin.readline

N = int(input())                # N(입력받을 수의 개수)
a = []                          # 빈리스트

for i in range(N):
    b = int(input())            #입력받은걸
    a.append(b)                 #a 리스트 에다 추가

a.sort(reverse=False)           # 오름차순으로 정렬

for i in a:                     # 정렬된걸 출력
    print(i)