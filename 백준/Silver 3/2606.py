n = int(input())
m = int(input())
# 컴퓨터 갯수만큼 생성
computers = [[] for _ in range(n+1)]

# 그래프 방식을 통해서 연결된 컴퓨터 리스트 생성
for __ in range(m):
    v1, v2 = map(int,input().split())
    computers[v1].append(v2)
    computers[v2].append(v1)
# 스택에 1번 컴퓨터와 연결된 리스트 생성
stack = list(computers[1])
# 방문 처리 생성
visited = [False] * (n+1)
# 스택값이 비어있을 동안 반복
while stack:
    # stack 의 값을 뽑아 current 에 넣어줌
    cur = stack.pop()
    # current 에 담겨있는 컴퓨터들 탐색
    for j in computers[cur]:
        # 방문처리 안했으면 탐색 후 방문처리 및 스택에 추가
        if visited[j] == False:
            visited[j] = True
            stack.append(j)
# 스택의 값이 0 이면 0 아닐경우 본인 컴퓨터 제외 출력
if visited.count(True) == 0:
    print(0)
else:
    print(visited.count(True)-1)