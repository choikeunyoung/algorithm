# import sys
# N,M = map(int,sys.stdin.readline().split())
# num_list = list(map(int,sys.stdin.readline().split()))
# total_list = []
# for _ in range(M):
#     i,j = map(int,sys.stdin.readline().split())
#     sum_ = 0
#     total_a = 0
#     total_b = 0
    

import sys
N,M = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
for i in range(len(num_list)-1):
    num_list[i+1] += num_list[i]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    if i == j:
        if i-1 == 0:
            print(num_list[j-1])
        elif i-1 != 0:
            print(num_list[j-1]-num_list[i-2])
    else:
        if i-1 == 0:
            print(num_list[j-1])
        elif i-1 != 0:
            print(num_list[j-1]-num_list[i-2])