#################백준 5622번 다이얼##################

import sys
input = sys.stdin.readline

N = input()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(a)):
    if a[i] in N:
        
        N = N.replace(a[i], "+")  #문자열에서 특정 문자 바꾸기
            

print(len(N)-1)