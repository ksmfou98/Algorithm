#### 백준 1181번 단어 정렬 ####

import sys
input = sys.stdin.readline


arr = []
N = int(input())

for i in range(N):
    a = input().split('\n')
    arr.append([len(a[0]), a[0]])
 
arr.sort(reverse=False)            #2차원 배열일 경우에 앞에꺼 비교해서 같으면 뒤에꺼 사전순으로 비교됨.

print(arr[0][1])

for i in range(1, len(arr)):
    if(arr[i][1] == arr[i-1][1]):
        continue
    print(arr[i][1], end="\n")