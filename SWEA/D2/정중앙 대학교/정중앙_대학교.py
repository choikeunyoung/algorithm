import heapq

N = int(input())
start = [500]
cnt = 1
for _ in range(N):
    A, B = map(int,input().split())
    cnt += 2
    check = []
    heapq.heappush(start,B)
    heapq.heappush(start,A)
    for i in range(cnt//2+1):
        check.append(heapq.heappop(start))
    print(check[-1])
    for i in check:
        heapq.heappush(start, i)