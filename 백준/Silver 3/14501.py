import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

day_list = []

for _ in range(N):
    day_list.append(list(map(int,input().split())))

for i in range(N-1,-1,-1):
    if i + day_list[i][0]<= N:
        dp[i] = max(dp[i+day_list[i][0]]+day_list[i][1],dp[i+1])
    else:
        dp[i] = dp[i+1]
print(max(dp))