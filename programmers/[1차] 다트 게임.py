def solution(dartResult):
    game_set_score = []
    current_score = 0
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            if dartResult[i + 1].isnumeric():
                game_set_score.append(current_score)
                current_score = int(dartResult[i] + dartResult[i + 1])

            elif dartResult[i - 1].isnumeric():
                continue

            else:
                game_set_score.append(current_score)
                current_score = int(dartResult[i])

        if dartResult[i] == "S":
            current_score = current_score ** 1

        if dartResult[i] == "D":
            current_score = current_score ** 2

        if dartResult[i] == "T":
            current_score = current_score ** 3

        if dartResult[i] == "*":
            current_score = current_score * 2
            game_set_score[-1] = game_set_score[-1] * 2

        if dartResult[i] == "#":
            current_score = current_score * (-1)

    game_set_score.append(current_score)

    return sum(game_set_score)