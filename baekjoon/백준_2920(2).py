import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

ascending = True
descending = True

for i in range(7):
    if num[i] < num[i+1]:
        descending= False
    elif num[i] > num[i+1]:
        ascending= False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")

