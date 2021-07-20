def solution(absolutes, signs):
    result = [num if sign else -num for num, sign in zip(absolutes, signs)]
    return sum(result)