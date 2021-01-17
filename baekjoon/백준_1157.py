#################백준 1157번 단어 공부##################



s = input()              #문자열 s를 입력받음
result = [0] * 26        #빈 리스트를 26개 만듬 ( A~Z가 26개임)

dohyun = s.upper()       #dohyun 변수에다가 s를 다 대문자로 바꿔버림
k = 0

for i in dohyun:         #빈리스트에다가 자기 아스키코드-65번쨰의 값에다가 1을 더해줌 ( 가장 많이쓰인 걸 찾기 위해)
    result[ord(i)-65] = result[ord(i)-65] + 1       #ord는 문자를 아스키코드로 표현
    
sum = result[0]     #sum은 가장 많이 쓰인 값이 뭔지 찾기위한 변수

for i in range(len(result)):
    for j in range(len(result)): ## sum에다가 리스트의 최댓값을 넣음
        if sum < result[i]:
            sum = result[i]


for i in range(len(result)):   # 리스트에서 sum이랑 같은게 있으면 k 에다가 1을더함
    if(result[i] == sum):      
        k = k + 1

if(k > 1):        #만약에 k가 1보다 크면 sum의 값이 2개이상 이라는것임 그럼 ? 출력
    print("?")
else:
    print(chr(result.index(sum)+65))   #chr은 아스키 코드를 문자로 표현 
    


            

    


