T = int(input())

dp = [1,1,1]

for i in range(3,101):
    dp.append(dp[i-3]+dp[i-2])

for tc in range(T):
    N = int(input())
    print(dp[N-1])