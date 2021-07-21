def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]
    match_count = 0

    for lotto in lottos:
        if lotto in win_nums:
            match_count += 1
    return [rank[match_count + lottos.count(0)], rank[match_count]]