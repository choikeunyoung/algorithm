import sys
# 많은 인풋 처리
input = sys.stdin.readline

N = int(input())
# 그래프 연결
graph = [ [] for _ in range(N+1)]
# 방문 처리
visited = [ 0 for _ in range(N+1) ]
# 양방향 그래프
for _ in range(N-1):
    S,E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
# 리프 노드 저장
leaf_node = []
# 리프 노드에 값 저장
for i in range(1,N+1):
    if len(graph[i]) == 1:
        leaf_node.append(i)
# 리프노드가 없을때까지 반복
while leaf_node:
    # 뽑아냄
    next = leaf_node.pop()
    # 연결된 그래프 노드 탐색
    for i in graph[next]:
        # 방문 했으면 무시
        if visited[i] == 1:
            continue
        # 그래프와 연결된 값들 순회
        for j in graph[i]:
            # j 노드와 i 노드의 연결을 제거
            graph[j].remove(i) # (1,2,3) i = 2 (1,3)
            # 제거한 노드와 개수가 1개인 경우 => 리프 노드
            if len(graph[j]) == 1:
                # 리프 노드에 값 추가
                leaf_node.append(j)
        # i 노드 방문 처리
        print(i)
        visited[i] = 1
        # i 노드와 연결된 그래프 초기화 위에서 연결을 제거했기 때문에
        graph[i] = []

print(sum(visited))