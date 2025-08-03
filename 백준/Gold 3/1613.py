import sys

input = sys.stdin.readline

N, M = map(int,input().split())
# N 개의 노드 생성
graph = [[0] * (N+1) for _ in range(N+1)]
# S 가 시작 E 가 끝으로 먼저 일어난 사건에 -1 늦게 일어난 노드에 1 저장
for _ in range(M):
    s, e = map(int,input().split())
    graph[s][e] = -1
    graph[e][s] = 1
# 플로이드-와샬 통해서 이전에 탐색한 노드랑 같은 값인지 체크해가며 행을 체크
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] != 0 and graph[i][k] == graph[k][j]:
                graph[i][j] = graph[i][k]

S = int(input())
# 각각의 값 출력
for _ in range(S):
    start, end = map(int, input().split())
    print(graph[start][end])