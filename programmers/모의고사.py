def solution(answers):
    score = {
        1 : 0,
        2 : 0,
        3 : 0,
    }
    
    one = [1,2,3,4,5] * 2000
    two = [2,1,2,3,2,4,2,5] * 1250
    three = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            score[1] += 1
        
        if answers[i] == two[i]:
            score[2] += 1
        
        if answers[i] == three[i]:
            score[3] += 1
    
    
    return [k for k,v in score.items() if max(score.values()) == v]
    
    