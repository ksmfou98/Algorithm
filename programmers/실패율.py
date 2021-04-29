# 0은 0으로 못나눈다 명심하자 !! 이거 떄문에 런타임에러로 막혔었음..

def solution(N, stages):
    fail = []
    result = []
    for i in range(1, N+1):

        x=0 # 분모
        y=0 # 분자
        for j in stages:
            if j == i:
                x += 1
            if j >= i:
                y += 1
        if x == 0 and y == 0:
            fail.append([i, 0])
        else:
            fail.append([i, x/y])
    
    fail.sort(reverse=True, key=lambda x: x[1])
    
    for i in range(N):
        result.append(fail[i][0])
    return result
