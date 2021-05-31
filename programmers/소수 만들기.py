from itertools import combinations
import math

def solution(nums):
    
    def numCheck(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    count = 0
    combination = list(combinations(nums, 3))
    for i in combination:

        if numCheck(i[0] + i[1] + i[2]):
            count += 1
    
    return count