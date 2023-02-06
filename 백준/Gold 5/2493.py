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

import sys

input = sys.stdin.readline

N = int(input())
# 타워들의 리스트를 받아옴
tower_list = list(map(int,input().split()))
# 정답을 출력할 리스트 생성
ans_list = [0]*N
# stack 리스트 생성
stack = []
# enumerate를 통해서 index 와 value 를 받아옴
for i,v in enumerate(tower_list):
    # stack 리스트가 존재할경우 반복문
    while stack:
    # stack에 저장된 마지막값과 현재의 value 값을 비교
        if stack[-1][1] > v:
    # stack 값이 더 큰 경우 ans_list의 i 번째 index에 stack의 index 값을 추가
            ans_list[i] = stack[-1][0] + 1
            break
    # 그 외의 경우 stack 값을 추출
        else:
            stack.pop()
    # stack에 i번째 index와 value 값 추가
    stack.append([i,tower_list[i]])

print(*ans_list)