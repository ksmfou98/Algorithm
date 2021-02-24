## 백준 4948: 베르트랑 공준    ## python3 으론 안되고 pypy3 으로 해야됨... python3 시간초과 샹,,

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



while 1:
    n = int(input())
    if n == 0:
        break
    li = []
    for i in range(n+1, (2*n)+1):
        if isPrime(i) == 1:
            li.append(i)
    print(len(li))