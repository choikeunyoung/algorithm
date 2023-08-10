# import sys
# from collections import deque
# 시간초과 코드

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     words = input().strip()
#     ans = deque()
#     current_pos = 0
#     for word in words:
#         if word == "<":
#             current_pos -= 1
#             if current_pos < 0:
#                 current_pos = 0
#         elif word == ">":
#             current_pos += 1
#             if current_pos >= len(ans):
#                 current_pos = len(ans)
#         elif word == "-":
#             if ans != "":
#                 ans.pop()
#         else:
#             if current_pos == 0:
#                 ans.appendleft(word)
#                 current_pos += 1
#             elif current_pos == len(ans):
#                 ans.append(word)
#                 current_pos += 1
#             else:
                        
#     print(ans)

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    words = input().strip()
    left_list, right_list = [], []
    last_ope = ""
    for word in words:
        if word == "<":
            if left_list:
                right_list.append(left_list.pop())
            last_ope = "<"
        elif word == ">":
            if right_list:
                left_list.append(right_list.pop())
            last_ope = ">"
        elif word == "-":
            if last_ope == ">":
                if left_list:
                    left_list.pop()
            elif last_ope == "<":
                if right_list:
                    right_list.pop()
        else:
            left_list.append(word)
    
    while right_list:
        left_list.append(right_list.pop())
    
    print("".join(left_list))