## 백준 2579번 계단 오르기 ###

import sys
input = sys.stdin.readline

N = int(input())

arr = [0]*301  # 계단 점수 저장 리스트
result = [0]*301 #현재 까지의 점수 합을 저장하는 리스트

for i in range(N):
    arr[i] = int(input())
   

result[0] = arr[0] #첫번째 계단에 오를때 까지의 점수의 합 = 첫번째 계단의 점수
result[1] = arr[1]+arr[0] #두번째 계단에 오를때의 점수의 최댓값 = 0번째 1번째 둘다 밟는 경우
result[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, N):
    result[i] = max(result[i-2]+arr[i], result[i-3]+arr[i-1]+arr[i])   ## i-3 이 핵심임.. 난 계속 i-1 로 접근해서 결국 못풀고 해설봤다.. 하..

print(result[N-1])