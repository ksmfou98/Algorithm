def solution(array, commands):

    result = []
    for s in range(len(commands)):
        answer = array
        i = commands[s][0]
        j = commands[s][1]
        k = commands[s][2]

        answer = answer[i-1:j]
        answer.sort(reverse=False)
        answer = answer[k-1]
        result.append(answer)
    return result