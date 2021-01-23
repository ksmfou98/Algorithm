#################백준 5622번 다이얼##################


import sys
input = sys.stdin.readline



def f(n):
    a = ord(n)

    if a >= 65 and a <= 67:
        return 3
    
    elif a >= 68 and a <=70:
        return 4

    elif a >= 71 and a <=73:
        return 5

    elif a >= 74 and a <=76:
        return 6
    
    elif a >= 77 and a <=79:
        return 7

    elif a >= 80 and a <=83:
        return 8

    elif a >= 84 and a <=86:
        return 9

    elif a >= 87 and a <=90:
        return 10
     
number = input()
sum = 0
for i in range(len(number)-1):
    sum += f(number[i])

print(sum)
    

