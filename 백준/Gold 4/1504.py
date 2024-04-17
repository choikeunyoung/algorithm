import sys
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())

matrix = [ [] for _ in range(N+1)]
distance = [10 ** 9] * (N+1)

for _ in range(M):
    S, E, W = map(int,input().split())
    matrix[S].append((W,E))
    matrix[E].append((W,S))

target_1, target_2 = map(int,input().split())


def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, matrix[start])
    while queue:
        dist, now = heapq.heappop(queue)
        if now == end:
            
            return 
        if distance[now] == 10 ** 9:
