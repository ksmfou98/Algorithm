def solution(brown, yellow):
    num = brown + yellow
    for i in range(3, num + 1):
        if num % i == 0 and num // i >= i and (num // i - 2) * (i - 2) == yellow:
            return [num // i, i]


# (a-2)*(b-2) == yellow 가 핵심 공식 이다.