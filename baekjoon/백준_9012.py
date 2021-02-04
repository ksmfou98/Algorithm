######### 9012번 괄호 ############

import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    a = input()
    left = 0
    right = 0
    for j in a:
        if j == '(':
            left += 1
        elif j == ')':
            right += 1
        if right > left:
            right += 999
        
    if left == right:
        print("YES")
    else:
        print("NO")
