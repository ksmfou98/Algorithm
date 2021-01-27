#################백준 2920번 음계 ###################

import sys
input = sys.stdin.readline

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]


a = list(map(int, input().split()))

if a == ascending:
    print("ascending")
elif a == descending:
    print("descending")
else:
    print("mixed")
