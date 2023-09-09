import heapq
import sys

input = sys.stdin.readline

N = int(input())
class_list = []

for _ in range(N):
    heapq.heappush(class_list, list(map(int, input().split())))
check = [heapq.heappop(class_list)[1]]

for i in range(N - 1):
    if check[0] > class_list[0][0]:
        heapq.heappush(check, heapq.heappop(class_list)[1])
    else:
        heapq.heappop(check)
        heapq.heappush(check, heapq.heappop(class_list)[1])
print(len(check))
