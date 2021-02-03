######### 2475번 검증수 ############

import sys
input = sys.stdin.readline


a, b, c, d, e = map(int, input().split())

result = (a*a) + (b*b) + (c*c) + (d*d) + (e*e)

print(result%10)