import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
M = int(input())

ans_list = [ [0] * N for _ in range(N)]

for i in range(N):
    ans_list[i][i] = 1

for i in range(N-1):
    j = i + 1
    if num_list[i] == num_list[j]:
        ans_list[i][j] = 1

if N > 2:
    for i in range(N):
        index = i
        for j in range(N:2:-1):
            



for _ in range(M):
    start, end = map(int,input().split())
    start -= 1
    end -= 1
    print(num_dict[start][end])