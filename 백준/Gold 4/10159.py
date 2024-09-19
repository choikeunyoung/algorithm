import sys

input = sys.stdin.readline

N = int(input())

M = int(input())
# 초기 그래프 선언
graph = [[0] * (N+1) for _ in range(N+1)]
# 들어온 인풋에 대해서 누가 더 큰지 체크
for _ in range(M):
    S,E = map(int,input().split())
    graph[S][E] = 1
# i,i 인덱스 0으로 초기화
for i in range(N+1):
    graph[i][i] = 0
# 플로이드 와샬
for i in range(1,N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            # j 에서 i 가 가는길이 있고 i 에서 k 로 가는 길이 있는 경우 j에서 k 로 가는 길이 존재 1 체크
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
# 갈 수 없는길 체크
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        # i 랑 j 랑 같은 경우 무시
        if i == j:
            continue
        # i 에서 j 로 갈 수 없고 j 에서 i 로 올 수 없는 경우 cnt 증가
        if graph[i][j] == 0 and graph[j][i] == 0:
            cnt += 1
    print(cnt)

print(graph)