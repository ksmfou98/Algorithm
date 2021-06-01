import math


def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if math.sqrt(i) == int(math.sqrt(i)):
            result -= i
        else:
            result += i

    return result


# 완전 제곱근은 약수가 홀수이고 아닌것은 약수가 짝수이다