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
# 많은 인풋 처리
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 인풋값 공백 제거 후
    words = input().strip()
    # 왼쪽 리스트 오른쪽 리스트 생성
    left_list, right_list = [], []
    # 반복문을 진행하며
    for word in words:
        # 만약 < 움직임이면 left 리스트 값이 있으면 right 리스트에 값추가
        if word == "<":
            if left_list:
                right_list.append(left_list.pop())
        # 만약 > 움직임이면 right 리스트 값이 있으면 left 리스트에 값추가
        elif word == ">":
            if right_list:
                left_list.append(right_list.pop())
        # 만약 - 이면 left 리스트 값이 있으면 pop
        elif word == "-":
            if left_list:
                left_list.pop()
        # left 리스트에 값을 계속 추가
        else:
            left_list.append(word)
    # right 리스트 값이 없어질때 까지 뽑아서 왼쪽 리스트에 값추가
    while right_list:
        left_list.append(right_list.pop())
    
    print("".join(left_list))