def solution(numbers):
    solve=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j:
                continue
            elif numbers[i]+numbers[j] in solve:
                continue
            else:
                solve.append(numbers[i]+numbers[j])
    solve.sort()
    answer = solve
    return answer