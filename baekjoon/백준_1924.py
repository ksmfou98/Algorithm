#################백준 1924 2007년 ###################

import sys
input = sys.stdin.readline

x, y = map(int, input().split())


def date(x):
    X = x - 1
    sum = 0
    while X != 0:
        if X == 1 or X == 3 or X == 5 or X == 7 or X == 8 or X == 10 or X == 12:
            sum += 31
        elif X == 2:
            sum += 28
        elif X == 4 or X == 6 or X == 9 or X == 11:
            sum += 30
        X -= 1
    return sum - 1


dohyun = date(x) + y
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(week[dohyun % 7])



