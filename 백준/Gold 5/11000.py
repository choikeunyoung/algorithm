import heapq
import sys

input = sys.stdin.readline

N = int(input())
class_list = []

for _ in range(N):
    heapq.heappush(class_list,list(map(int,input().split())))
cnt = 1
check = [heapq.heappop(class_list)]
list_length = 1
while class_list:
    ans = heapq.heappop(class_list)
    for i in range(list_length):
        if check[i][-1] >= ans[0]:
            check[i] = ans
            break
    else:
        check.append(ans)
print(ans)