def solution(n):
    n = str(n)
    result = []
    for i in range(len(n)-1, -1, -1):
        result.append(int(n[i]))
        
    return result
        