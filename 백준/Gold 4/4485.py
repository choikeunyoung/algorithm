import heapq
import sys

input = sys.stdin.readline

direction = [(0,-1),(-1,0),(0,1),(1,0)]

def dijkstra():
    queue = [(matrix[0][0],(0,0))]
    distance[0][0] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        for k in range(4):
            ny = now[0] + direction[k][0]
            nx = now[1] + direction[k][1]
            if 0 <= nx < N and 0 <= ny < N:
                dist = cost + matrix[ny][nx]
                if dist < distance[ny][nx]:
                    distance[ny][nx] = dist
                    heapq.heappush(queue,(dist,(ny,nx)))

index = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        matrix = [ list(map(int,input().split())) for _ in range(N)]
        distance = [[10**9] * (N) for _ in range(N) ]
    dijkstra()
    print(f"Problem {index}: {distance[N-1][N-1]}")
    index += 1