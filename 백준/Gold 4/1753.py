import sys
from collections import defaultdict

V, E = map(int,input().split())

start = int(input())

matrix = defaultdict(list)

for _ in range(E):
    S, E, W = map(int,input().split())
    matrix[S].append((E, W))

visited = [False] * (V+1)
distance = [10**9] * (V+1)

for i in matrix[start]:
    distance[i[0]] = i[1]



for i in range(V-1):
    current = 0
    for k in range(1, V+1):
