import sys
# 재귀 제한
sys.setrecursionlimit(10000)
# DFS 실행
def DFS(start):
    global max_value
    global N
    # 온 경로가 방문한 곳일 경우
    if visited[start[0]][start[1]] != 0:
        # 현재 돌아온 경로를 리턴
        return visited[start[0]][start[1]]
    # 시작 값 1로 초기화
    visited[start[0]][start[1]] = 1
    for k in range(4):
        ny = direction[k][0] + start[0]
        nx = direction[k][1] + start[1]
        # 범위 내에 있는 경우
        if 0 <= ny < N and 0 <= nx < N:
            # 다음 가야할 값이 현재 값보다 작은 경우
            if matrix[ny][nx] < matrix[start[0]][start[1]]:
                # 재귀 실행 하며 현재 값이랑 재귀해서 돌아온 값 + 1 한 값을 갱신
                visited[start[0]][start[1]] = max(visited[start[0]][start[1]],DFS((ny,nx))+1)
    # 최종적으로 갱신된 현재 위치값 반환
    return visited[start[0]][start[1]]


input = sys.stdin.readline

N = int(input())

direction = [(0,-1),(-1,0),(0,1),(1,0)]

matrix = []
max_value = 0
visited = [[0] * (N) for _ in range(N) ]

for _ in range(N):
    matrix.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        # 방문하지 않았을 경우 DFS 실행
        if visited[i][j] == 0:
            max_value = max(max_value,DFS((i,j)))

print(max_value)