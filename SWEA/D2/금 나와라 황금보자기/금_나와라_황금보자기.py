import heapq

N = int(input())

gold_list = list(map(int,input().split()))

for v in range(len(gold_list)):
    gold_list[v] = (gold_list[v],0)

heapq.heapify(gold_list)
cnt = 0

while gold_list:
    A = heapq.heappop(gold_list)
    if A[-1] == 1:
        print(cnt)
        break
    else:
        cnt += 1
    if gold_list:
        B = heapq.heappop(gold_list)
        if B[-1] == 1:
            print(cnt)
            break
        else:
            cnt += 1
    heapq.heappush(gold_list,(B[0]*2,1))