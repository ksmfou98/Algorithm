def solution(numbers, target):
    from collections import deque
    first_queue = [numbers[0], -1*numbers[0]]
    queue = deque(first_queue)
    for n in numbers[1:]:
        curLen = len(queue)
        for i in range(curLen):
            curNum = queue.popleft()
            queue.append(curNum+n)
            queue.append(curNum-n)
    return queue.count(target)
            
        
            
        


# queue = [-1, +3, +1, -3]    numbers = [3,4,5]
# numbers : [1,2,3,4,5]
# target : [8]

## bfs  넓이 우선 탐색 !
# if result == target -> count +=1
# if result > target  -> break
#            -1            +1
#         -3    +1       -1   +3
#       -6  0  -2 +4