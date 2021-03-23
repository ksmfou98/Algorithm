import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
	a = input().split()
	if a[0] == "i":
		stack.append(int(a[1]))
	elif a[0] == "o":
		if len(stack) == 0:
			print("empty")
		else:
			print(stack[len(stack)-1])	
			stack.pop()
	elif a[0] == "c":
		print(len(stack))