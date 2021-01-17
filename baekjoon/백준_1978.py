#################백준 1978번 소수 찾기##################


N = int(input())                         #입력 받을 수의 갯수
                       
numbers = map(int, input().split())      #공백을 기준으로 input 받음
a = list(numbers)                        #input 받은 numbers를 list로 변경함

count = 0                                #소수일 때 카운트 해줄 변수 생성

for i in a:                              #리스트값에 순차 접근
    test = 0                             #약수 갯수 담을 변수
    for j in range(1, i+1):              #1부터 자기 자신까지 접근
        if i % j == 0:                   #자기 자신 % (1~자기자신) 나눠서 0이면
            test += 1                    #약수 갯수 추가
     
    if test == 2:                        #약수 갯수가 2개이면
        count += 1                       # 소수갯수 추가

print(count)
    

