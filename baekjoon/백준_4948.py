## 백준 4948: 베르트랑 공준    

import sys
import math
input = sys.stdin.readline



def isPrime(a):
    if(a<2):
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            return False
    return 1

N = [0] * 246915
for i in range(2, 246915):
    if isPrime(i) == 1:
        N[i] = 1
        

while 1:
    n = int(input())
    if n == 0:
        break
    
    count = 0
    for i in range(n+1, (2*n)+1):
        if N[i] == 1:
            count += 1
    print(count)
    