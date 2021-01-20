#################백준 2798번  블랙잭##################

import sys

input = sys.stdin.readline

N, M = map(int, input().split())    # N(카드의 개수)  M(비교할 값)
a = list(map(int, input().split())) # a( N개의 카드 값들을 입력받아서 a에다 리스트로 저장)
b = len(a)     # b는 a리스트의 개수
result = 0     # 최종 결과를 출력할 변수

for i in range(0,b-2):                   #  ex) 5, 6, 7, 8, 9 일때 3개의 합이 21과 가장 비슷한 값구해야댐
    for j in range(i+1,b-1):             # 그럼 3개의 합이니깐 3중 for문을 사용해서
        for k in range(j+1,b):           # 첫번째가 5 이고 두번쨰가 6 일떄 세번째가 7 8 9 이런식으로 하나하나 합을 구함
            if a[i] + a[j] + a[k] > M:   # 그 합이 M보다 크면 그냥 패스
                continue
            else:                        # M 보다 작을떈 result에 저장할꺼임 , 그런데 저장되어있던 result보다 커야만 result에 저장
                result = max(result, a[i] + a[j] + a[k]) # 그 이유는 M과 가장 가까운 값을 출력하기 위해서임


print(result)