#################백준 10872번  팩토리얼##################



import sys
input = sys.stdin.readline           #두줄 필수로 작성해야 시간 단축됨

N = int(input())                     #입력받음

def factorial(N):                    # N의 값이 들어오면
    if N == 0:                       # N이 0일땐 1 반환
        return 1

    else:                            # 그게아니면 N 에서 계속 내려가는 재귀함수 생성
        return N * factorial(N-1)

print(factorial(N))