# import sys

# input = sys.stdin.readline

# N = int(input())
# tower_list = list(map(int,input().split()))
# ans_list = [0]*N
# for j in range(N-1,-1,-1):
#     ans = tower_list.pop()
#     ans_index = j
#     for i in range(len(tower_list)-1,-1,-1):
#         if tower_list[i] > ans:
#             ans_list[j] = i+1
#             break
#         else:
#             ans_list[j] = 0

# print(*ans_list)

# import sys

# input = sys.stdin.readline

# N = int(input())
# tower_list = list(map(int,input().split()))
# ans_list = [0]*N
# stack = []
# for i,v in enumerate(tower_list):
#     while stack:
#         if stack[-1][1] > v:
#             ans_list[i] = stack[-1][0] + 1
#             break
#         else:
#             stack.pop()
#     stack.append([i,tower_list[i]])
            
# print(*ans_list)


import sys

input = sys.stdin.readline

N = int(input())
tower_list = list(map(int,input().split()))
ans_list = [0]*N
stack = []
for i in range(N-1,-1,-1):
    j = i
    while stack:
        if stack[-1][1] < tower_list[j]:
            ans_list[i+1] = j+1
            stack.pop()
            break
        else:
            j -= 1
            if j < 0:
                break
    stack.append([i+1,tower_list.pop()])
            
print(*ans_list)