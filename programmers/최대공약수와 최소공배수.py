def solution(n, m):
    
    
    def gcd(n, m):
        while 1:
            if n % m == 0:
                return m
            else:
                c = n % m
                n = m
                m = c
    
    def lcm(n, m):
        return n*m // gcd(n,m)
    
    return [gcd(n,m), lcm(n,m)]
        