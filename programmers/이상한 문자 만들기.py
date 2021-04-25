def solution(s):
    result = []
    count = 0
    for i in s:
        if i == " ":
            count = 0
            result.append(" ")
            continue
        
        if count % 2 == 0:
            result.append(i.upper())
            
        if count % 2 == 1:
            result.append(i.lower())
            
        count += 1
        
    result = "".join(result)
    return result
        