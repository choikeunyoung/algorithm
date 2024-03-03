import sys
import heapq

input = sys.stdin.readline
# 시작점을 기준으로 다익스트라 시작
def BFS(init):
    # queue 리스트 생성
    queue = []
    # 우선순위 큐 생성
    heapq.heappush(queue,(0,init))
    distance[init] = 0
    # queue 가 빌때까지 실행
    while queue:
        # queue에 거리, 노드 순으로 저장
        dist, now = heapq.heappop(queue)
        # 노드의 거리가 현재 거리보다 작은경우 무시
        if distance[now]<dist:
            continue
        # 외의 경우 현재 노드와 연결된 노드를 반복
        for i in matrix[now]:
            # 현재 거리 + 연결된 노드의 가중치 증가
            cost = dist + i[0]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[1]]:
                # 거리 값을 최소값으로 갱신
                distance[i[1]]=cost
                # queue 리스트에 가중치, 노드 순으로 저장
                heapq.heappush(queue,(cost,i[1]))

V, E = map(int,input().split())

distance = [10**9] * (V+1)
start = int(input())

matrix = [[] for _ in range(V+1)]

for _ in range(E):
    S, E, W = map(int,input().split())
    matrix[S].append((W, E))

BFS(start)

for i in range(1,V+1):
    if distance[i] == 10**9:
        print("INF")
    else:
        print(distance[i])