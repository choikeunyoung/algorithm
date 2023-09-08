import heapq
import sys

input = sys.stdin.readline

N = int(input())
class_list = []

for _ in range(N):
    heapq.heappush(class_list,list(map(int,input().split())))

check = [heapq.heappop(class_list)]
list_length = 1
while class_list:
    ans = heapq.heappop(class_list)
    