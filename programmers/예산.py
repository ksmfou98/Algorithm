def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if budget - i < 0:
            break
        count += 1
        budget -= i
    
    return count