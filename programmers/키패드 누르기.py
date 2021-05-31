def solution(numbers, hand):
    num = [
        [3, 1],
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 1],
        [1, 2],
        [2, 0],
        [2, 1],
        [2, 2],
    ]
    left = [1, 4, 7]
    right = [3, 6, 9]
    middle = [2, 5, 8, 0]
    result = []
    leftHand = [3,0]
    rightHand = [3,2]
    for i in numbers:
        if i in left:
            result.append("L")
            leftHand = num[i]
        if i in right:
            result.append("R")
            rightHand = num[i]
        if i in middle:
            if (abs(leftHand[1] - num[i][1]) + abs(leftHand[0] - num[i][0])) > (
                abs(rightHand[1] - num[i][1]) + abs(rightHand[0] - num[i][0])
            ):
                result.append("R")
                rightHand = num[i]
            elif (abs(leftHand[1] - num[i][1]) + abs(leftHand[0] - num[i][0])) < (
                abs(rightHand[1] - num[i][1]) + abs(rightHand[0] - num[i][0])
            ):
                result.append("L")
                leftHand = num[i]
            else:
                if hand == "right":
                    result.append("R")
                    rightHand = num[i]
                else:
                    result.append("L")
                    leftHand = num[i]
    return "".join(result)


