#### 백준 1158번 요세푸스 문제 ####

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []
result = []
for i in range(N):
    arr.append(i+1)

S = K-1

print("<", end="")

while(len(arr) > S):                          # S보다 클경우 
    result.append(arr[0+S])
    arr[len(arr):len(arr)+S] = arr[0:0+S]
    del arr[0]
    del arr[0:0+S]


k = 0
while 1:                                      #나머지 경우
    for i in range(len(arr)):
        k += 1
        if k == K :
            result.append(arr[i])
            k = 0
            del arr[i]
    
    if len(arr) == 0:
        break

for i in range(len(result)):
    print(result[i], end="")
    if i == len(result)-1:
        print(">")
    else:
        print(",", end=" ")
        


       