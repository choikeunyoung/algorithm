import sys
import heapq

input = sys.stdin.readline
# 다익스트라 알고리즘
def dijkstra(start):
    # q 초기화
    q = []
    # heapq 로 q 리스트 생성
    heapq.heappush(q,(0,start))
    # distance로 초기 시작점 0 으로 초기화
    distance[start] = 0
    # q 값이 존재할 경우 반복문 진행
    while q:
        # 거리, 현재 값으로 값을 뽑아냄
        dist, now = heapq.heappop(q)
        # 저장된 거리가 현재 값보다 작은 경우 다음 반복문
        if distance[now] < dist:
            continue
        # 연결된 (가중치, 노드값) 반복
        for i in graph[now]:
            # 비용에 현재 값 + 가중치 더해줌
            cost = dist + i[0]
            # 비용이 거리보다 작은 경우
            if cost < distance[i[1]]:
                # 거리 값 갱신
                distance[i[1]] = cost
                # 비용과 노드 추가
                heapq.heappush(q,(cost,i[1]))

N, M = map(int,input().split())

distance = [10 ** 9] *(N+1)
graph = [[]for _ in range(N+1)]

for _ in range(M):
    S,E,W = map(int,input().split())
    graph[S].append((W,E))
    graph[E].append((W,S))

S,T = map(int,input().split())

dijkstra(S)
print(distance[T])