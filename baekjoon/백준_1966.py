## 백준_1966번 : 프린터 큐

import sys
input = sys.stdin.readline


T = int(input())

for i in range(T):
    N, M = map(int, input().split())  # N : 문서의 개수  M : 궁금한 문서가 현재 몇번째에 있는지
    arr = list(map(int, input().split()))
    count = M
    dodo = [0] * N
    dodo[M] = 1
    check = arr[M]

    cnt = 0
    while True:
        if arr[0] == max(arr) and arr[0] == check and dodo[0] == 1:
            cnt += 1
            break
        elif arr[0] == max(arr):
            arr.remove(arr[0])
            dodo.remove(dodo[0])
            cnt += 1
        else:
            arr.append(arr[0])
            dodo.append(dodo[0])
            arr.remove(arr[0])
            dodo.remove(dodo[0])

    print(cnt)