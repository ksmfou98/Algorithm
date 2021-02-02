#### 백준 10989번 수 정렬하기 3 ####

import sys
input = sys.stdin.readline


N = int(input())

b = [0] * 10001     #메모리가 적게 주어지면 sort함수보단 이런식으로 만들어서 사용하는걸 하자!

for i in range(N):
    a = int(input())
    b[a] += 1


for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)

