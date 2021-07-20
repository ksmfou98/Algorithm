def solution(nums):
    return min((len(nums) // 2), len(list(set(nums))))
