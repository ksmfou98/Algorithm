## 백준 1475번 : 방 번호
import sys
input = sys.stdin.readline

num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

N = input()

for i in range(len(N)-1):
    if int(N[i]) == 6:
        num[9] += 1
    else:
        num[int(N[i])] += 1

if max(num) == num[9] and num.index(max(num)) == 9:
    if max(num) % 2 == 0:
        print(max(num)//2)
    else:
        print((max(num)//2) + 1)
else:
    print(max(num))

