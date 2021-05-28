import math
from itertools import permutations


def solution(numbers):
    count = 0
    result = []

    def sosuCheck(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    for j in range(1, len(numbers) + 1):
        num = list(map("".join, permutations(list(numbers), j)))
        num = list(map(int, num))
        result.extend(num)

    result = list(set(result))

    for i in result:
        if sosuCheck(i):
            count += 1

    return count

