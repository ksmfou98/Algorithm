def solution(n):
    answer = ''
    a = "수박"
    answer = a*(n//2)
    if n % 2 == 1:
        answer = answer + a[0]
    return answer