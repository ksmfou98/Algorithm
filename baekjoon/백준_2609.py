#### 백준 2609번 최대공약수와 최소공배수 ####

import sys
input = sys.stdin.readline

A, B = map(int,input().split())


def gcd(A, B):   # 유클리드 호제법 이용했음 ( A, B 의 최대 공약수는 B와 A%B의 최대공약수와 같음)
    if A % B == 0:
        # print(B)
        return B
    else:
        return gcd(B, A%B)




if A > B :
    result = gcd(A,B)
    print(result)
else:
    result = gcd(B,A)
    print(result)

print(A*B // gcd(A, B))  ## 최대공배수는 두수를 곱한뒤 최대공약수로 나눠주면됌.