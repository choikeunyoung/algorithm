import sys
input = sys.stdin.readline

N = int(input())
stack = []
stack_length = 0
for _ in range(N):
    char = list(map(str,input().split()))
    if char[0] == "push":
        stack.append(char[1])
        stack_length += 1
    elif char[0] == 'top':
        if stack_length == 0:
            print(-1)
        else:
            print(stack[-1])
    elif char[0] == 'size':
        print(stack_length)
    elif char[0] == 'pop':
        if stack_length == 0:
            print(-1)
        else:
            print(stack.pop())
            stack_length -= 1
    elif char[0] == 'empty':
        if stack_length == 0:
            print(1)
        else:
            print(0)