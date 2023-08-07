import sys

input = sys.stdin.readline

N = int(input())
num_list = []
value = 1

for _ in range(N):
    num_list.append(int(input()))

stack = []
answer = ["+"]
index = 0

for i in range(N*2 - 1):
    if value < N:
        stack.append(value)
        value += 1
        answer.append("+")
    if stack[-1] == num_list[index]:
        answer.append("-")
        stack.pop()
        index += 1
    else:
print(answer)
if stack:
    print("NO")
else:
    for j in answer:
        print(j)