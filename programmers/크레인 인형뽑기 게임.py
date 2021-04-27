def solution(board, moves):
    result = []
    score = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue

            if len(result) > 0:
                if result[len(result) - 1] == board[j][i - 1]:
                    score += 2
                    result.pop()
                    board[j][i - 1] = 0
                    break

            result.append(board[j][i - 1])
            board[j][i - 1] = 0
            break

    return score
