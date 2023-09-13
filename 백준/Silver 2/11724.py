import sys

input = sys.stdin.readline


# DFS 시행
def DFS(start):
    visited[start] = True
    stack = graph[start]
    while stack:
        check = stack.pop()
        if not visited[check]:
            visited[check] = True
            stack.extend(graph[check])


# 노드와 간선의 갯수 입력
N, M = map(int, input().split())
# graph 형태로 생성
graph = [[] for _ in range(N + 1)]
# 방문처리 체크 리스트
visited = [False] * (N + 1)
for _ in range(M):
    # A, B 를 받아옴
    A, B = map(int, input().split())
    # 방향이 없으므로 양쪽에 추가
    graph[A].append(B)
    graph[B].append(A)

cnt = 0
# N+1 까지 반복을 시행하며 DFS 를 시행 한 횟수 체크
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1
print(cnt)
