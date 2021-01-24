#################백준 1316번 그룹 단어 체커##################

import sys
input = sys.stdin.readline

N = int(input())
count = 0
for i in range(N):
    a = input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            continue
        else:
            if a.find(a[j],j+1) == -1:
                continue
            else:
                count += 1
                break

print(N-count)