## 백준_10814번 : 나이순 정렬

import sys
input = sys.stdin.readline


N = int(input()) #회원의 수

arr = []
count = 1
for i in range(N):
    age, name = input().split()
    age = int(age)
    arr.append([age, name, count])
    count += 1

arr.sort(key=lambda x: (x[0], x[2])) #정렬 , 만약 x[0] 이 같으면 x[2]로 비교



for i in range(N):
    print(arr[i][0], arr[i][1])