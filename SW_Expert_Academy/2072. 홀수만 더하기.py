import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = 0
    for i in arr:
        if i % 2 == 1:
            result += i
    
    print(f'#{test_case} {result}')
