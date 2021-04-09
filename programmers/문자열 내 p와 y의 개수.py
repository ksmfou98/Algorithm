def solution(s):
    ss = s.lower()
    count_p = 0
    count_y = 0
    for alphabet in ss:
        if alphabet == "p":
            count_p += 1
        elif alphabet == "y":
            count_y += 1
        else:
            continue
    if count_y == count_p:
        return True
    else:
        return False