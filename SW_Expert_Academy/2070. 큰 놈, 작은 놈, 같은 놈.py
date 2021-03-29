T = int(input())
for test_case in range(1, T + 1):
    x, y = map(int, input().split())
    if x > y:
        print(f"#{test_case} >")      
    elif x == y:
        print(f"#{test_case} =")      
    else:
        print(f"#{test_case} <")      
   