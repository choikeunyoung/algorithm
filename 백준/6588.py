import sys

input = sys.stdin.readline

def pri_num():
    num_list = [True] * 1000000

    for i in range(2,round(len(num_list)**0.5)):
        if i%2 == 1:
            if num_list[i] == True:
                for j in range(2*i, len(num_list), i):
                    num_list[j] = False

    return[ x for x in range(2,len(num_list)) if (num_list[x] and x%2 == 1)]

pri_list = pri_num()

print(len(pri_list))
# while True:
#     ans_num = int(input())
#     if ans_num == 0: break
#     flag = 0
#     for k in range(0,len(pri_list)):
#         for l in range(k, len(pri_list)):
#             if ((pri_list[k] + pri_list[l]) == ans_num):
#                 flag = 1
#                 break
#             elif ((pri_list[k] + pri_list[l] > ans_num)):
#                 break
#         if flag == 1:
#             print(ans_num,"=",pri_list[k],"+",pri_list[l])
#             break
#     else:
#         print("Goldbach's conjecture is wrong.")