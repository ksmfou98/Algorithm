def solution(x):
    result = []
    for i in list(str(x)):
        result.append(int(i))
        
    s = sum(result)
    
    if x % s == 0:
        return True
    else:
        return False
        