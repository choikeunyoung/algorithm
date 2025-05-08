dp = [[0] * 4 for _ in range(10001)]

dp[0][1] = 1
dp[0][2] = 1
dp[0][3] = 1

for i in range(1, 10001):
    if i - 1 >= 0:
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][1] = 0
        
    if i - 2 >= 0:
        dp[i][2] = dp[i][1] + dp[i-2][2]
    else:
        dp[i][2] = dp[i][1]

    if i - 3 >= 0:
        dp[i][3] = dp[i][2] + dp[i-3][3]
    else:
        dp[i][3] = dp[i][2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][3])