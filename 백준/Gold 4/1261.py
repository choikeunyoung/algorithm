import heapq

N,M = map(int,input().split())

matrix = [ list(map(int,input())) for _ in range(M) ]

direction = [(0,-1), (-1,0), (0,1), (1,0)]
distance = [ [10**9]*N for _ in range(M) ]

def dijkstra():
    queue = (1, (0,0))
    distance[0][0] = 1
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now[0]][now[1]] < dist:
            continue

        for k in range(4):  
            ny = now[0] + direction[k][0]
            nx = now[1] + direction[k][1]
            if 0 <= ny < M and 0 <= nx < N:
                