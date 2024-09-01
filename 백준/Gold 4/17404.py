import sys

input = sys.stdin.readline


N = int(input())

dp = [0] * (N+1)

for _ in range(N):
    