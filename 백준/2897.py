N,M = map(int,input().split())

matrix = [ list(map(str,input())) for _ in range(N) ]
# # = 빌딩, X = 주차된 차, . 빈 주차 공간

dx = [1, 0, 1]
dy = [0, 1, 1]
zero_cnt = 0
one_cnt = 0
two_cnt = 0
three_cnt = 0
four_cnt = 0
for i in range(N-1):
    for j in range(M-1):
        x_cnt = 0
        dot_cnt = 0
        # 시작이 . 였을 경우
        if matrix[i][j] == '.':
            dot_cnt += 1
            for k in range(len(dx)):
                x = i + dx[k]
                y = j + dy[k]
                if (x >= 0 and y >= 0) and (x < N and y < M):
                    if matrix[x][y] == '.':
                        dot_cnt += 1
                    elif matrix[x][y] == 'X':
                        x_cnt += 1
                    else:
                        x_cnt = 0
                        dot_cnt = 0
                        break
            if x_cnt == 0 and dot_cnt == 0:
                pass
            else:
                if x_cnt == 0 and dot_cnt == 4:
                    zero_cnt += 1
                elif x_cnt == 1 and dot_cnt == 3:
                    one_cnt += 1
                elif x_cnt == 2 and dot_cnt == 2:
                    two_cnt += 1
                elif x_cnt == 3 and dot_cnt == 1:
                    three_cnt += 1
        # 시작이 'X' 였을 경우
        elif matrix[i][j] == 'X':
            x_cnt += 1
            for k in range(len(dx)):
                x = i + dx[k]
                y = j + dy[k]
                if (x >= 0 and y >= 0) and (x < N and y < M):
                    if matrix[x][y] == '.':
                        dot_cnt += 1
                    elif matrix[x][y] == 'X':
                        x_cnt += 1
                    else:
                        x_cnt = 0
                        dot_cnt = 0
                        break
            if x_cnt == 0 and dot_cnt == 0:
                pass
            else:
                if x_cnt == 1 and dot_cnt == 3:
                    one_cnt += 1
                elif x_cnt == 2 and dot_cnt == 2:
                    two_cnt += 1
                elif x_cnt == 3 and dot_cnt == 1:
                    three_cnt += 1
                elif x_cnt == 4 and dot_cnt == 0:
                    four_cnt += 1
        else:
            pass
else:
    print(zero_cnt)
    print(one_cnt)
    print(two_cnt)
    print(three_cnt)
    print(four_cnt)