import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
# 추가되는 돈 : P원 (A사)
# 추가되는 돈 : S원 (B사)
# 기본 요금 : Q
# 월간 사용량 : R
# 사용하는 리터 : W
a_company = 0
b_company = 0
for i in range (1, T+1):
    p,q,r,s,w = map(int,sys.stdin.readline().split())
    a_company = p*w
    if w <= r:
        b_company = q
    else:
        b_company = q+((w-r)*s)
    
    if a_company > b_company:
        print(f"#{i}", b_company)
    elif a_company < b_company:
        print(f"#{i}", a_company)


# T = int(input())
# # 추가되는 돈 : P원 (A사)
# # 추가되는 돈 : S원 (B사)
# # 기본 요금 : Q
# # 월간 사용량 : R
# # 사용하는 리터 : W
# a_company = 0
# b_company = 0
# for i in range (1, T+1):
#     p,q,r,s,w = map(int,input().split())
#     a_company = p*w
#     if w <= r:
#         b_company = q
#     else:
#         b_company = q+((w-r)*s)
    
#     if a_company > b_company:
#         print(f"#{i}", b_company)
#     elif a_company < b_company:
#         print(f"#{i}", a_company)