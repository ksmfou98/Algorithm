## 백준 _ 10773번 : 제로
import sys
input = sys.stdin.readline


K = int(input())
arr = []
for i in range(K):
    n = int(input())
    if n == 0:
        arr.pop()  #맨 마지막 요소 삭제
        continue
    arr.append(n)

print(sum(arr))
    