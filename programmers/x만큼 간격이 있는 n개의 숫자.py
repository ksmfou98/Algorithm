def solution(x, n):
    if x*n < 0:
        return [i for i in range(x, x*n-1, x)]
    elif x*n == 0:
        return [0]*n
    return [i for i in range(x, x*n+1, x)]