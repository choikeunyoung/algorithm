import heapq
# 다익스트라
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        # 시간, 현재 위치 뽑아냄
        time, now = heapq.heappop(queue)
        # +1 한 값
        next_add = now+1
        #  -1 한 값
        next_min = now-1
        # *2 한 값
        next_multi = now*2
        # + 했을때 100,000 범위 이내일 경우
        if next_add <= 100000:
            # 시간이 더 적은 경우 값 갱신 후 추가
            if distance[next_add] > time + 1:
                distance[next_add] = time + 1
                heapq.heappush(queue, (time+1, next_add))
        # - 했을때 0보다 크거나 같은 경우
        if next_min >= 0:
            # 시간이 더 적게 소요된 경우 갱신 후 추가
            if distance[next_min] > time + 1:
                distance[next_min] = time + 1
                heapq.heappush(queue, (time+1, next_min))
        # * 했을때 100,000 범위 이내일 경우
        if next_multi <= 100000:
            # 시간이 더 적게 소요된 경우 갱신 후 추가
            if distance[next_multi] > time:
                distance[next_multi] = time
                heapq.heappush(queue, (time, next_multi))

start, target = map(int,input().split())
#  시작과 목표값이 같은경우 0
if start == target:
    print(0)
else:
    # 외의 경우 다익스트라 시행
    distance = [10**9] * 100001

    dijkstra(start)

    print(distance[target])