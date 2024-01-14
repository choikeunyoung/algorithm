import sys

input = sys.stdin.readline

N = int(input())

beer = []
for _ in range(N):
    beer.append(int(input()))
if N == 1:
    print(beer[0])
elif N == 2:
    print(beer[1] + beer[0])
else:
    dp = [beer[0], beer[1] + beer[0]]
    dp.append(max(beer[1] + beer[2], beer[0] + beer[2]))

    for i in range(3, N):
        dp.append(max(beer[i] + beer[i - 1] + dp[i - 3], beer[i] + dp[i - 2]))

    print(max(dp))
