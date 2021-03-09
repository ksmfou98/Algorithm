import math

def solution(n):
    answer = 0
    if n == 2:
        return 1
    for i in range(2, n+1):
        count = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            answer += 1          


    return answer