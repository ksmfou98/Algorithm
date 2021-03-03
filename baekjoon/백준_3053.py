## 백준 3053번 : 택시 기하학


import sys
import math
input = sys.stdin.readline


pi = 3.141592653589793238

R = int(input())

ucli = pi * R * R
texi = float(R * R * 2)

print(round(ucli, 6))
print(round(texi, 6))