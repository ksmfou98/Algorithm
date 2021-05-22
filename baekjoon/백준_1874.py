import sys
input = sys.stdin.readline

n = int(input())
result = []
returnResult = []
store = [] 


for i in range(n):
    x = int(input())
    result.append(x)

for i in range(1, n+1):
    store.append(i)
    returnResult.append("+")

    while len(store) >= 1:
        if store[-1] == result[0]:
            del store[-1]
            del result[0]
            returnResult.append("-")
        else :
            break

if len(store) == 0:
    print('\n'.join(returnResult))
else :
    print("NO")




