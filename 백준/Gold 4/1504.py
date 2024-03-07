import sys
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())

matrix = [ [] for _ in range(N)]

for _ in range(M):
    S, E, W = map(int,input().split())
    matrix[S].append((W,E))
    matrix[E].append((W,S))

target

def dijkstra():
