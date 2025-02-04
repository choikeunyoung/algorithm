import sys

input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    num_list.append(list(map(int,input().split())))

num_list.sort()

dp = [0]*N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if num_list[j][1] < num_list[i][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(N - max(dp))

# 최대한 전기줄을 많이 연결하는 경우의 수 = 제거해야 하는 전기줄 수