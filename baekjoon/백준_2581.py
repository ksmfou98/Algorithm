#################백준 2581번 소수 ###################

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

result = []


for i in range(N, M+1):
    count = 0
    if i > 10 and i % 2 == 0:
        continue
    elif  i > 10 and i % 3 == 0:
        continue
    elif  i > 10 and i % 5 == 0:
        continue
    elif  i > 10 and i % 7 ==0:
        continue
    for j in range(1, i):
      
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 1:
        result.append(i)
    
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))

