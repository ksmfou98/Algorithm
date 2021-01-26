#################백준 11718번 그대로 출력하기 ###################

while True:
    try:
        print(input())
    except EOFError:  ## ctrl + z  or ctrl +d 가 들어오면 종료되게하는 예외처리
        break