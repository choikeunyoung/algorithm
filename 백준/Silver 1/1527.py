# # A,B = map(int,input().split())
# # cnt = 0
# # num_list = ['4','7']
# # for i in range(A,B+1):
# #     for j in str(i):

# ## 보류
# # import sys
# # input = sys.stdin.readline

# def dfs(k):
#     global cnt
#     if len(str(k)) > y:
#         return
#     if x <= len(str(k)) <= y:
#         if a <= k <= b:
#             cnt += 1
#     for i in 4, 7:
#         num = k * 10 + i
#         print(num)
#         dfs(num)
# a, b = map(int, input().split())
# x = len(str(a))
# y = len(str(b))
# cnt = 0
# dfs(4)
# dfs(7)
# print(cnt)
# 재귀 함수
def DFS(num):
    # cnt 변수 글로벌 선언
    global cnt
    # num 값에 "4" or "7" 추가
    num = str(num)
    # 범위 내에 있으면 cnt 증가
    if A <= int(num) <= B:
        cnt += 1
    # B보다 크면 재귀 종료
    if int(num) > B:
        return
    # 그 외의 경우 문자열로 4, 7 붙여가며 재귀 시행
    else:
        for i in ["4", "7"]:
            DFS(num+i)
    
A, B = map(int,input().split())
cnt = 0
# 초기갑 4로 시작, 7로 시작한 값들 계산
DFS(4)
DFS(7)
print(cnt)