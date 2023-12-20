import sys
input = sys.stdin.readline

N = int(input())
total = 0
# stack 에 쌓을 리스트 생성
stack = []
for _ in range(N):
    tower = int(input())
    if stack:
        while stack and stack[-1] <= tower:
            stack.pop()
        stack.append(tower)
        total += len(stack) - 1
    else:
        stack.append(tower)
print(total)