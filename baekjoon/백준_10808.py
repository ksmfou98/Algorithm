## 백준 10808번 : 알파벳 개수

import sys
input = sys.stdin.readline

alpha = [0] * 26

S = input().strip()  # strip() 은 뒤에 \n을 지워줌
for i in S:

    alpha[ord(i)-97] += 1

for i in alpha:
    print(i, end=" ")


