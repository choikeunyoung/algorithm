import sys
# 많은 인풋값 처리
input = sys.stdin.readline
# DFS 탐색
def DFS(start):
    stack = graph[start]
    visited[start] = True
    # 몇번째 방문했는지 체크해줄 변수
    cnt = 1
    visited_dict[start] = 1
    while stack:
        # stack 에 값을 뽑아내며
        check = stack.pop()
        # 방문하지 않았을 경우
        if not visited[check]:
            # cnt 증가 후
            cnt += 1
            # 딕셔너리에 cnt 값 넣어줌
            visited_dict[check] = cnt
            # 방문처리
            visited[check] = True
            # stack 증가
            stack.extend(graph[check])

N, M, R = map(int,input().split())

graph = [ [] for _ in range(N+1) ]
# 방문 리스트 갯수
visited = [False]*(N+1)
# 방문 딕셔너리
visited_dict = {}

for _ in range(M):
    # 무방향 그래프이므로 양방향으로 추가
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
# 들어온 값을 오름차순으로 정렬함 => pop 을 사용하기 때문에 오름차순
for i in graph:
    i.sort()
# 1 ~ N 까지 몇번째 방문한 것인지 체크할 딕셔너리 생성
for i in range(1,N+1):
    visited_dict[i] = 0
# DFS 실행
DFS(R)
# 딕셔너리 key, value 값 출력
for i in range(1, N+1):
    print(visited_dict[i])