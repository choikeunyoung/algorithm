import sys
from collections import defaultdict

V, E = map(int,input().split())

start = int(input())

matrix = defaultdict(list)

for _ in range(E):
    S, E, W = map(int,input().split())
    matrix[S].append([E, W])

for i in range(1,V+1):
    