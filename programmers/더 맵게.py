import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while 1:
        if scoville[0] >= K:
            return count
        if len(scoville) < 2:
            return -1
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        shake = x1 + (x2 * 2)
        heapq.heappush(scoville, shake)
        count += 1