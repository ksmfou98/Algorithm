import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
firstNum = nlist[-1]
secondNum = nlist[-2]


sumNum = firstNum * K + secondNum
quotient, remainder = divmod(M, K+1)

result = (sumNum * quotient) + (firstNum * remainder)

print(result)
