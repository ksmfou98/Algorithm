#################백준 2292번 벌집##################

import sys
input = sys.stdin.readline

N = int(input())     
sum = 1         #범위를 정해줄 변수
i = 1           #6의 배수만큼 증가 시켜줄 변수 (벌집 규칙이 6의 배수만큼 늘어남)
count = 1       #이동한 칸의 수
while 1:
    if N <= sum:                      # 1     -> 1번지남
        break                         # 2~7   -> 2번지남
    else:                             # 8~19  -> 3번지남
        sum = sum + 6*i               # 20~37 -> 4번지남
        i += 1                        # 38~61 -> 5번지남
        count += 1                    # 오른쪽 값이 sum = sum + 6*i  의 역할
                                      # N이 sum보다 작으면 반복문 탈출 후에 count 출력
print(count)