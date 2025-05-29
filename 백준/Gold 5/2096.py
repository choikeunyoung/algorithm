import sys

input = sys.stdin.readline

N = int(input())

first = list(map(int,input().split()))

max_dp = first
min_dp = first
# 최대값 최소값 저장
for _ in range(N-1):
    a, b, c = map(int,input().split())
    max_a = max(max_dp[0],max_dp[1]) + a
    max_b = max(max_dp[0], max_dp[1], max_dp[2]) + b
    max_c = max(max_dp[1], max_dp[2]) + c
    min_a = min(min_dp[0], min_dp[1]) + a
    min_b = min(min_dp[0], min_dp[1], min_dp[2]) + b
    min_c = min(min_dp[2], min_dp[1]) + c
    max_dp = [max_a, max_b, max_c]
    min_dp = [min_a, min_b, min_c]

print(max(max_dp), min(min_dp))
