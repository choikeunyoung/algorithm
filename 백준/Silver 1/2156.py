import sys

input = sys.stdin.readline

N = int(input())

beer = []

for _ in range(N):
    beer.append(int(input()))

dp = [[(beer[0],1),(0,0)]]

for i in range(1,N):
    