## 백준 5585번 : 거스름돈

import sys
input = sys.stdin.readline

N = int(input())

result = 1000 - N   
li = [500, 100, 50, 10, 5, 1]
count = 0

for i in li:
    count = count + (result // i)
    result = result % i

print(count)


    