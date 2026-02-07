import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())
# 공백 제거
matrix = [list(input().rstrip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, dist):
    global answer
    # 목표에 도달 했을때 거리가 K 와 같으면
    if x == 0 and y == C - 1:
        if dist == K:
            answer += 1
        return
    # 거리가 K 보다 크면 돌아가기
    if dist >= K:
        return
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내에 있고 방문 안했하고 벽이 아닌경우 방문 처리 후 재귀
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and matrix[nx][ny] != "T":
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                # 백트래킹
                visited[nx][ny] = False


visited[R - 1][0] = True
dfs(R - 1, 0, 1)

print(answer)
