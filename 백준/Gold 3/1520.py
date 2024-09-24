import sys
# 재귀 제한 해제
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N, M = map(int,input().split())

matrix = []
# 방문 체크
visited = [[-1] * M for _ in range(N)]

for _ in range(N):
    matrix.append(list(map(int,input().split())))

direction = [(0,-1),(-1,0),(0,1),(1,0)]
# 백트래킹
def backtracking(start):
    global cnt
    # 끝에 도달하면 1 리턴
    if start[0] == N-1 and start[1] == M-1:
        return 1
    # -1 외의 값인 경우 경로를 탐색한 적 있기 때문에 현재 위치값 리턴
    if visited[start[0]][start[1]] != -1:
        return visited[start[0]][start[1]]
    # 4방향 탐색한 값 저장
    road = 0
    # 4방향 탐색
    for k in range(4):
        ny = direction[k][0] + start[0]
        nx = direction[k][1] + start[1]
        # 조건에 만족하 경우 깊이 탐색 하며 리턴값 반환
        if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] < matrix[start[0]][start[1]]:
            road += backtracking((ny,nx))
    # 현재 위치에 경로 탐색을 통해 얻은 값 저장
    visited[start[0]][start[1]] = road
    # 현재 위치값 반환
    return visited[start[0]][start[1]]
# 끝에 도달하는 점 1로 갱신
visited[N-1][M-1] = 1
backtracking((0,0))
print(visited[0][0])