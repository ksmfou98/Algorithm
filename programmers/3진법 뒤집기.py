from collections import deque

def solution(n):
    ThreeNumber = deque([])
    result = 0
    while True:
        ThreeNumber.appendleft(n%3)
        if n // 3 == 0:
            break
        n = n // 3
    
    ThreeNumber.reverse()
    length = len(ThreeNumber)
    
    for i in ThreeNumber:
        result += i*(3**(length-1))
        length -= 1

    
    return result