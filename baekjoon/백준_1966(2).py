import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())  # N : 문서의 개수  M : 찾을 문서의 위치
    printQueue = list(map(int, input().split()))
    printQueue = [(i, idx) for idx, i in enumerate(printQueue)]
    count = 0 # 몇번째로 출력되는지 세는 카운트

    while 1:
        if printQueue[0][0] == max(printQueue, key=lambda x: x[0])[0]:
            count += 1
            if printQueue[0][1] == M:
                print(count)
                break
            printQueue.pop(0)
        else:
            printQueue.append(printQueue.pop(0))



T = int(input())
for i in range(T):
    solution()