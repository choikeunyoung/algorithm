import heapq

T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int,input().split())
    graph = [ [] for _ in range(N+1)]
    for _ in range(M):
        start, end, weight = map(int,input().split())
        graph[start].append((weight,end))
    print(graph)