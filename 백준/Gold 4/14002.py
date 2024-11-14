N = int(input())

num_list = list(map(int,input().split()))

dp = [0] * N
path = [0] * N
dp[0] = 1
path[0] = -1
dp_length = 0
max_value = 1
max_index = 0

for i in range(1,N):
    dp[i] = 1
    path[i] = -1
    value = 0
    for j in range(i):
        if num_list[i] > num_list[j]:
            if dp[j] > value:
                value = dp[j]
                path[i] = j
    if max_value < value + 1:
        max_value = value + 1
        max_index = i
    dp[i] = max(dp[i],value + 1)

answer = []

while max_index != -1:
    answer.append(num_list[max_index])
    max_index = path[max_index]

answer.reverse()
print(max_value)
print(*answer)