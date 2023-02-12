import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
ans_list = [-1]*N
stack = []

for i,v in enumerate(num_list):
    while stack:
        if stack[-1][1] < v:
            ans_list[stack[-1][0]] = v
            stack.pop()
        else:
            break
    stack.append([i,num_list[i]])
print(*ans_list)