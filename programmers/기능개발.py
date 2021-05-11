def solution(progresses, speeds):

    result = []
    while len(progresses) > 0:
        count = 0

        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        while len(progresses) > 0:
            if progresses[0] >= 100:
                count += 1
                del progresses[0]
                del speeds[0]
            else:
                break
        if count > 0:
            result.append(count)
    return result


