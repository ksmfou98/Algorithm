#################백준 2908번 상수 ##################

import sys
input = sys.stdin.readline


N, M = map(int, input().split())

def reverseNum(n):                   #역순으로 바꾸는 함수
    a = []                           #빈 리스트 생성
    while 1:                         
        if n <= 0:                   #n이 0보다 작거나 같으면 탈출
            break
        else:        
            a.append(n%10)           #빈리스트에 1의자리부터 추가
            n = n // 10              
    
    sum = 0
    count = 1
    for i in range(len(a)-1, -1, -1):         #리스트를 숫자로 바꾸는 반복문
        sum = sum + a[i]*count
        count = count * 10

    return sum

if reverseNum(M) > reverseNum(N):
    print(reverseNum(M))
else:
    print(reverseNum(N))



    
    
    
    
    
    
    

