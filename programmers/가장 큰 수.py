def solution(numbers):
    strNumbers = []
    for i in numbers:
        strNumbers.append(str(i))
    if sum(numbers) == 0:
        return "0"
    return ''.join(sorted(strNumbers, key=lambda x: x*3, reverse=True))