import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
y = 0
        
for i in range(1,T+1):
    cnt = 1
    check_list=[]
    x = int(sys.stdin.readline())
    while True:
        y = x*cnt
        y = str(y)
        for j in y:
            if j not in check_list:
                check_list.append(j)
        if len(check_list) == 10:
            print(x*cnt)
            break
        cnt += 1



# T = int(input())
# y = 0
# for i in range(1,T+1):
#     cnt = 1
#     check_list=[]
#     x = int(input())
#     while True:
#         y = x*cnt
#         y = str(y)
#         for j in y:
#             if j not in check_list:
#                 check_list.append(j)
#         if len(check_list) == 10:
#             print(f'#{i}', x*cnt)
#             break
#         cnt += 1