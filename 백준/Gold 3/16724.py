import sys

input = sys.stdin.readline
# 방향 배열 탐색
def DFS(index):
    # 몇번째 DFS진행인지 체크
    global safe_cnt
    stack = [index]
    while stack:
        check = stack.pop()
        # 다음 위치를 dictionary를 통해서 받아옴
        next = direction[matrix[check[0]][check[1]]]
        # 다음 위치 갱신
        ny = next[0] + check[0]
        nx = next[1] + check[1]
        # 현재 위치 safe_cnt 변수로 체크
        answer[check[0]][check[1]] = safe_cnt
        # 다음 위치가 가지 않았을 경우 스택에 추가
        if answer[ny][nx] == -1:
            stack.append((ny,nx))
    # 반복문이 끝난 후 answer라는 위치체크 배열에서 ny,nx 값과 마지막으로 뽑은 check 값을 비교하여 같은 사이클인지 체크
    # 같은 사이클인 경우 1이라는 값을 반환해줌
    if answer[ny][nx] == answer[check[0]][check[1]]:
        return 1
    # 다른 사이클의 경우 0 을 반환
    else:
        return 0

N, M = map(int,input().split())

matrix = [ list(map(str,input())) for _ in range(N)]
answer = [ [-1] * (M) for _ in range(N) ]

direction = {
    "D" : (1, 0),
    "L" : (0, -1),
    "R" : (0, 1),
    "U" : (-1, 0)
}

safe_cnt = 0
cnt = 0
for i in range(N):
    for j in range(M):
        # 방문 했는지 안했는지 -1로 체크
        if answer[i][j] == -1:
            # 방문 안했으면 DFS를 돌린 후 check값을 cnt에 더해줌 ( 같은 사이클의 경우 안전영역 체크로 1을 더해줌 )
            check = DFS((i,j))
            cnt += check
            safe_cnt += 1
print(cnt)