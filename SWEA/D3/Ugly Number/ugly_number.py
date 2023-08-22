import heapq

K = int(input())

num_list = list(map(int,input().split()))

DP = [1]
ans = []
max_num = max(num_list)

while len(ans) <= max(num_list):
    check = heapq.heappop(DP)
    if check not in ans:
        ans.append(check)
        heapq.heappush(DP,check*2)
        heapq.heappush(DP,check*3)
        heapq.heappush(DP,check*5)

for k in num_list:
    print(ans[k-1], end = " ")