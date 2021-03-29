T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = sum(arr) / 10
    result = round(result)
    print(f"#{test_case} {result}")
