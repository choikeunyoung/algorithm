A = input().strip()
B = input().strip()
C = input().strip()

a, b, c = len(A), len(B), len(C)

dp = [[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]

# LCS 3차원 비교
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            if A[i-1] == B[j-1] == C[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(
                    dp[i-1][j][k],
                    dp[i][j-1][k],
                    dp[i][j][k-1]
                )

print(dp[a][b][c])