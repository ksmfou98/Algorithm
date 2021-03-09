def solution(n):
    num=set(range(2,n+1))              # set 함수로 2~n까지의 수를 만들어서 num에 저장

    for i in range(2,n+1):
        if i in num:                   # 2부터 접근 시작 
            num-=set(range(2*i,n+1,i)) # num에있는 i의 배수를 지워줌 
    return len(num)                    # set 함수로 만든건 대박이다.. 


n = int(input())
print(solution(n))