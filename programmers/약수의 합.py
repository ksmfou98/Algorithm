def solution(n):
    if n == 1:
        return 1

    result = []
    for i in range(1, n//2):
        if n % i == 0:
            result.append(i)
            result.append(n//i)

    result = set(result)
    return sum(result)