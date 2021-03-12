## 백준 2455번 : 지능형 기차

import sys
input = sys.stdin.readline

person = [0] * 5

for i in range(4):
    out, come = map(int, input().split())
    person[i+1] = person[i] - out + come

print(max(person))