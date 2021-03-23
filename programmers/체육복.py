def solution(n, lost, reserve):
    count = n - len(lost)

    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            count += 1


    for i in lost:
        if i-1 in reserve:
            count += 1
            reserve.remove(i-1)
            continue
        if i+1 in reserve:
            count += 1
            reserve.remove(i+1)
            continue
        if i in reserve:
            count += 1
            reserve.remove(i)
            continue

    return count