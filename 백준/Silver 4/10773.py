import sys

input = sys.stdin.readline

K = int(input())

stack = []

for _ in range(K):
    check = int(input())
    # 들어온 값이 0 인 경우 stack 에서 뽑음
    if check == 0:
        if stack:
            stack.pop()
    else:
        stack.append(check)
# 만약 스택에 값이 있으면 스택의 모든 값의 합을 출력
if stack:
    print(sum(stack))
else:
    print(0)