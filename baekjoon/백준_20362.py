#################백준 20362번 유니대전 퀴즈쇼##################

import sys
input = sys.stdin.readline   # 이 두줄을 입력하면 실행 속도가 더 빨라짐.

N, S = input().split()       # N(채팅 개수) S(닉네임)  우선 둘다 문자열로 받고 N은 따로 정수 설정해줄거임

a = []                       # 빈 리스트 생성
k = 0                        # S닉네임의 인덱스 찾기위한 변수임
count = 0                    # 아쉬운 사람 명수를 카운트 하기 위한 변수
 
for i in range(int(N)):                         # 채팅 갯수 많큼 반복
    first, second = map(str,input().split())    # 공백을 기준으로 문자열 입력받음
    a.append([first, second])                   # 입력받은 문자열을 a의 2차원 리스트로 넣음
    if a[i][0] == S:                            # 만약에 방금 입력받은 값의 행의 0열에 S의 채팅이 있으면
        k = i                                   # 그 인덱스를 k의 저장

for i in range(k):                              # 0부터 s의 채팅이 있기 바로 전까지 접근함
    if a[i][1] == a[k][1]:                      # 그 사이의 s의 채팅과 똑같이 친 채팅이 있으면
        count += 1                              # 카운트 증가

print(count)
