#################백준 10817번 세 수##################

import sys
input = sys.stdin.readline

a = list(map(int, input().split()))

a.remove(max(a))
print(max(a))


