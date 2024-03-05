import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

matrix = [ [] for _ in range(N+1)]
# 다익스트라 거리
distance = [10**9] * (N+1)

for _ in range(M):
    S, E, W = map(int,input().split())
    matrix[S].append((W,E))
# 시작점과 끝점
start, target = map(int,input().split())    
# 다익스트라 알고리즘
def dijkstra(start):
    # 시작하는 값의 코스트는 0 이고 시작점이 주어지므로 queue 초기값 선언
    queue = [(0,start)]
    # 초기 거리 0 으로 설정
    distance[start] = 0
    # queue 값이 빌때까지
    while queue:
        # 거리, 노드 순으로 저장했기 때문에 출력
        dist, now = heapq.heappop(queue)
        # 노드의 거리가 현재 가지고있는 값보다 작은경우 다음 반복문
        if distance[now] < dist:
            continue
        # 노드와 연결된 노드들 탐색
        for next in matrix[now]:
            # cost 라는 변수에 현재 노드의 가중치 + 연결된 노드의 가중치 값 계산
            cost = dist + next[0]
            # 만약 연결된 노드의 가중치보다 cost 값이 작은 경우 값 갱신 후 가중치, 노드번호 추가
            if distance[next[1]] > cost:
                distance[next[1]] = cost
                heapq.heappush(queue,(cost, next[1]))

dijkstra(start)

print(distance[target])