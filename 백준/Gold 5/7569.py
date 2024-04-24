import sys
from collections import deque

input = sys.stdin.readline

N, M, H = map(int,input().split())

tomato = [ list(map(int,input().split())) for _ in range(M*H) ]

direction = [(-1,0), (0,1), (1,0), (0,-1)]

tomato_list = deque([])
# 일수 체크
day = 0
# 0의 개수 체크
zero_cnt = 0
# 익은 토마토 위치와 익지않은 토마토 개수 체크
for i in range(M*H):
    for j in range(N):
        if tomato[i][j] == 1:
            tomato_list.append((i,j))
        elif tomato[i][j] == 0:
            zero_cnt += 1
# 익지 않은 토마토가 없는 경우 바로 종료
if zero_cnt == 0:
    print(0)
    exit()
# 몇번 반복할지 몰라서 계속 반복
while True:
    # 임시 저장할 리스트
    check_list = deque([])
    # 토마토 위치가 없을때까지 반복
    while tomato_list:
        check = tomato_list.popleft()
        # 고른 토마토 위치가 몇번째 높이인지 체크
        range_check = check[0] // M
        # 방향배열 탐색
        for k in range(4):
            ny = direction[k][0] + check[0]
            nx = direction[k][1] + check[1]
            # 범위 내에 존재할 경우
            if (0 <= ny < M*H) and (0 <= nx < N):
                # 현재 고른 위치 내에서만 탐색
                if range_check * M <= ny < (range_check + 1) * M:
                    # 익지않은 토마토인 경우 토마토 익히고 개수 -1 후 위치 추가
                    if tomato[ny][nx] == 0:
                        tomato[ny][nx] = 1
                        zero_cnt -= 1
                        check_list.append((ny,nx))
        # 현재 뽑은 위치에서 위아래 층 도 익힘
        nh = check[0] + M
        nmh = check[0] - M

        if 0 <= nh < M*H:
            if tomato[nh][check[1]] == 0:
                tomato[nh][check[1]] = 1
                zero_cnt -= 1
                check_list.append((nh,check[1]))
    
        if 0 <= nmh < M*H:
            if tomato[nmh][check[1]] == 0:
                tomato[nmh][check[1]] = 1
                zero_cnt -= 1
                check_list.append((nmh,check[1]))
    # 더이상 토마토를 체크할 수 없을 때 반복문 탈출
    if not check_list and not tomato_list:
        break
    # 외의 경우 임시 저장한 리스트를 토마토 리스트에 추가 후 하루가 지남
    else:
        tomato_list = check_list
        day += 1
# 만약 반복문이 끝난 후 토마토가 익지않은 것이 있을 경우 -1 출력
if zero_cnt == 0:
    print(day)
else:
    print(-1)