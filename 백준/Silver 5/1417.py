import sys

input = sys.stdin.readline

N = int(input())

vote_list = []

for _ in range(N):
    vote_list.append(int(input()))

while True:
    