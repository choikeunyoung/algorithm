import sys
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int,input().split())

start = int(input())

martix = defaultdict(list)

for _ in range(E):
    S, E, W = map(int,input().split())
    martix[S].append([E, W])

print(martix)