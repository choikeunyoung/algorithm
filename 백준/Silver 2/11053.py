N = int(input())

num_list = list(map(int,input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))