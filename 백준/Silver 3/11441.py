import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int,input().split()))

total_list = [0] * (N+1)

for i in range(N):
    total_list[i+1] += total_list[i] + num_list[i]

M = int(input())

for _ in range(M):
    A,B = map(int,input().split())
    print(total_list[B]-total_list[A-1])