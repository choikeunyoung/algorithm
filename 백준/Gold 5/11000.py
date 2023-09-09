import heapq
import sys

input = sys.stdin.readline

N = int(input())
class_list = []

for _ in range(N):
    heapq.heappush(class_list, list(map(int, input().split())))

check = [heapq.heappop(class_list)]
list_length = 1
while class_list:
    flag = 0
    ans = heapq.heappop(class_list)
    for i in range(list_length):
        if check[i][-1] > ans[0]:
            flag = 1
        else:
            flag = 0
            check[i] = ans
            break
    if flag == 1:
        check.append(ans)
        list_length += 1
print(list_length)
