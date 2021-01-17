################백준 2675번 문자열 반복##################



T = int(input())           # 테스트 케이스 갯수

for i in range(T):
    result = []                 # 빈 리스트 생성
    R, S = input().split()      # R(1<=R<=8)각 테스트 케이스 반복 횟수   
                                # S(1<=S<=20) 문자열
    

    for j in S:                  # 문자열 S를 순차 접근함
        for k in range(int(R)):  # R을 아까 문자열로 입력 받았기떄문에 형변환 해줌
            result.append(j)     # 리스트 result 에다가 순차접근한 문자열S를 R번만큼 넣음 
    
    print(''.join(result))        # --> 리스트 result를 문자열로 표현 





    

   
        









