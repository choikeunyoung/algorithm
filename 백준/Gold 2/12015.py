def binary_search(index,value):
    left = 0
    middle = 0
    while left < index:
        middle = (left + index) // 2
        if dp[middle] < value:
            left = middle + 1
        else:
            index = middle
    return index

N = int(input())

num_list = list(map(int,input().split()))
dp_length = 0
dp = [0] * N
dp[0] = num_list[0]

for i in range(1,N):
    if num_list[i] > dp[dp_length]:
        dp_length += 1
        dp[dp_length] = num_list[i]
    elif num_list[i] < dp[dp_length]:
        change_value = binary_search(dp_length,num_list[i])
        dp[change_value] = num_list[i]
print(dp_length+1)