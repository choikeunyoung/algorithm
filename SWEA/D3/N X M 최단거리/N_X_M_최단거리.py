import heapq

N, M = map(int,input().split())

direction = [(0,-1),(-1,0),(0,1),(1,0)]

matrix = [ list(map(int,input().split())) for _ in range(N) ]

dist = [[float('inf')] * M for _ in range(N)]

def dijkstra():
    pq = []
    dist[0][0] = matrix[0][0]
    heapq.heappush(pq, (matrix[0][0], 0, 0))
    while pq:
        cost, y, x = heapq.heappop(pq)
        if dist[y][x] < cost:
            continue
        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]
            if (0 <= ny < N) and (0 <= nx < M):
                nextcost = cost + matrix[ny][nx]
                if dist[ny][nx] <= nextcost:
                    continue
                dist[ny][nx] = nextcost
                heapq.heappush(pq, (nextcost, ny, nx))
    return list(dist)

print(dijkstra())