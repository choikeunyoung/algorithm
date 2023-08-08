# DFS 구현 함수
def DFS(graph, N, V):
    # N의 길이만큼 방문 체크
    visited = [False] * N
    # graph 값들을 내림차순 정렬
    for i in graph:
        i.sort(reverse=True)
    # stack 변수에 graph[시작노드][전체를 얕은 복사] 해주지 않으면 graph 자체가 수정되버림
    stack = graph[V-1][:]
    # 처음 시작노드 True 처리
    visited[V-1] = True
    # 처음 노드 answer 리스트에 저장
    answer = [V]
    while stack:
        # stack 을 계속해서 뽑아내며
        next_node = stack.pop()
        # 방문하지 않으면 stack 에 추가 및 visited 방문처리 후 answer 에 저장
        if not visited[next_node]:
            stack.extend(graph[next_node])
            visited[next_node] = True
            answer.append(next_node+1)
    return answer

# 너비 우선 탐색 함수
def BFS(graph, N, V):
    # N 만큼 방문 체크 리스트
    visited = [False] * N
    # 그래프 값들을 오름차순 정렬
    for i in graph:
        i.sort()
    # stack 에 그래프 시작노드를 얕은 복사
    stack = graph[V-1][:]
    # visited 시작값을 True 처리
    visited[V-1] = True
    # answer에 시작값 넣기
    answer = [V]
    while stack:
        # 첫번째 값들을 계속해서 뽑아줌
        next_node = stack.pop(0)
        # 방문하지 않았으면
        if not visited[next_node]:
            # 다음 노드를 추가, 방문처리, answer 리스트 값 추가
            stack.extend(graph[next_node])
            visited[next_node] = True
            answer.append(next_node+1)
    return answer
    

N, M, V = map(int,input().split())

node_list= []
graph = [[] for _ in range(N)]

for _ in range(M):
    nodes = list(map(int,input().split()))
    graph[nodes[0]-1].append(nodes[1]-1)
    graph[nodes[1]-1].append(nodes[0]-1)
    
BFS_ans = BFS(graph, N, V)
DFS_ans = DFS(graph, N, V)

print(*DFS_ans)
print(*BFS_ans)