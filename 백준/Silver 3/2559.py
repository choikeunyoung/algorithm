import sys

N,K = map(int,input().split())
temp_list = list(map(int,input().split()))
max_temp = -sys.maxsize
sum_list = []
for i in range(N):
    if len(sum_list) == 0:
        sum_list.append(temp_list[i])
    else:
        sum_list.append(sum_list[i-1]+temp_list[i])
if K == 1:
    print(max(temp_list))
else:
    if sum_list[K-1] > max_temp:
        max_temp = sum_list[K-1]
    for i in range(N-K):
        if sum_list[i+K]-sum_list[i] > max_temp:
            max_temp = sum_list[i+K]-sum_list[i]
    print(max_temp)