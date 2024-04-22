import sys
from collections import deque

input = sys.stdin.readline

N, M, H = map(int,input().split())

tomato = [ list(map(int,input().split())) for _ in range(M*H) ]

direction = [(-1,0), (0,1), (1,0), (0,-1)]

tomato_list = deque([])

day = 0
zero_cnt = 0
for i in range(M*H):
    for j in range(N):
        if tomato[i][j] == 1:
            tomato_list.append((i,j))
        elif tomato[i][j] == 0:
            zero_cnt += 1

if zero_cnt == 0:
    print(0)
    exit()

while True:
    check_list = deque([])
    while tomato_list:
        check = tomato_list.popleft()
        for k in range(4):
            ny = direction[k][0] + check[0]
            nx = direction[k][1] + check[1]
            if (0 <= ny < M*H) and (0 <= nx < N):
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    zero_cnt -= 1
                    check_list.append((ny,nx))
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

    if not check_list and not tomato_list:
        break
    else:
        tomato_list = check_list
        day += 1

if zero_cnt == 0:
    print(day)
else:
    print(-1)