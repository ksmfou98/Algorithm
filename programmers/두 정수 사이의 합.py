def solution(a, b):
    answer = 0
    if a > b:
        (a, b) = (b, a)
    if a == b:
        return a
    for i in range(a, b + 1):
        answer += i
    return answer