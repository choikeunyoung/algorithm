import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def BFS(init):
    queue = deque(matrix[init])
    visited[init] = True
    for i in matrix[init]:
        distance[i[0]] = i[1]

    while queue:
        now, dist = queue.popleft()

        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in matrix[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                queue.append((i[0],cost))

V, E = map(int,input().split())

visited = [False] * (V+1)
distance = [10**9] * (V+1)
start = int(input())

matrix = defaultdict(list)

for _ in range(E):
    S, E, W = map(int,input().split())
    matrix[S].append((E, W))

BFS(start)

for i in range(1,V+1):
    if i != start:
        if distance[i] == 10**9:
            print("INF")
        else:
            print(distance[i])
    else:
        print(0)