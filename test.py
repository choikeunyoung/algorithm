from pprint import pprint

N = int(input())

matrix = [ [0] * (N+1) for _ in range(N+1) ]

graph = [ [] for _ in range(N+1) ]

for _ in range(10):
    A, B = map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)
    matrix[A][B] = 1
    matrix[B][A] = 1

print(graph)
pprint(matrix)