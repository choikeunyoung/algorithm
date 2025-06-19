import sys
import heapq

input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    num_list.append(tuple(map(int,input().split())))

num_list.sort()

ans = []
ans_length = 0

for num in num_list:
    heapq.heappush(ans,num[1])
    ans_length += 1
    if ans_length > num[0]:
        heapq.heappop(ans)
        ans_length -= 1

print(sum(ans))