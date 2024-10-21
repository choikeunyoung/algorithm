import sys

input = sys.stdin.readline
# 백트래킹
def DFS(start):
    # 최대값 저장
    global max_value
    # 값 저장
    global value
    # 최종 11에 도달했을 때
    if start == 11:
        # 최대 값보다 값이 크면 갱신
        if max_value < value:
            max_value = value
        return
    # 11명의 포지션 바복
    for j in range(11):
        # 포지션 값이 0 이 아니고 방문안했을 경우
        if position[start][j] != 0 and pos_visited[j] == False:
            # 방문 처리 후 값 더해주고 재귀 실행 백트래킹
            pos_visited[j] = True
            value += position[start][j]
            DFS(start+1)
            value -= position[start][j]
            pos_visited[j] = False

T = int(input())
# 테스트 케이스 반복문 만큼 진행
for _ in range(T):
    # 포지션별 리스트 추가
    position = []
    for _ in range(11):
        position.append(list(map(int,input().split())))
    # 최대값 기본 값
    max_value = 0
    value = 0
    # 방문처리 체크
    pos_visited = [False] * 11
    # 백트래킹
    for i in range(11):
        if position[0][i] != 0:
            pos_visited[i] = True
            value += position[0][i]
            DFS(1)
            value -= position[0][i]
            pos_visited[i] = False
    print(max_value)