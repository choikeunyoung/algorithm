import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

matrix = [ [] for _ in range(N+1)]
distance = [10**9] * (N+1)

for _ in range(M):
    S, E, W = map(int,input().split())
    matrix[S].append((W,E))

start, target = map(int,input().split())    

def dijkstra(start):
    queue = [(0,start)]
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next in matrix[now]:
            cost = dist + next[0]
            if distance[next[1]] > cost:
                distance[next[1]] = cost
                heapq.heappush(queue,(cost, next[1]))


dijkstra(start)

print(distance[target])