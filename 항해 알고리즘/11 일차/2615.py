matrix = [list(map(int, input().split())) for _ in range(19)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for i in range(19):
    cnt = 0
    check = 0
    for j in range(19):
        if matrix[i][j] == 1:
            for l in range(len(dx)):
                for k in range(len(dx)):
                    x = i + dx[l]  # 정해진 방향으로 일직선으로 있어야기 때문에 한번만
                    y = j + dy[k]
                    if (x >= 0 and y >= 0) and (x <= 18 and y <= 18):
                        if matrix[x][y] == 1:
                            cnt = 2  # cnt 2
                            x += dx[l]
                            y += dy[k]
                            if (x >= 0 and y >= 0) and (x <= 18 and y <= 18):
                                if matrix[x][y] == 1:
                                    cnt += 1  # cnt 3
                                    x += dx[l]
                                    y += dy[k]
                                    if (x >= 0 and y >= 0) and (x <= 18 and y <= 18):
                                        if matrix[x][y] == 1:
                                            cnt += 1  # cnt 4
                                            x += dx[l]
                                            y += dy[k]
                                            if (x >= 0 and y >= 0) and (
                                                x <= 18 and y <= 18
                                            ):
                                                if matrix[x][y] == 1:
                                                    cnt += 1  # cnt 5
                                                    nx = x + dx[l]
                                                    ny = y + dy[k]
                                                    if (
                                                        (
                                                            i - dx[l] >= 0
                                                            and j - dy[k] >= 0
                                                        )
                                                        and (
                                                            i - dx[l] <= 18
                                                            and j - dy[k] <= 18
                                                        )
                                                        and matrix[i - dx[l]][j - dy[k]]
                                                        == 1
                                                    ):
                                                        cnt = 0
                                                    if (nx >= 0 and ny >= 0) and (
                                                        nx <= 18 and ny <= 18
                                                    ):
                                                        if matrix[nx][ny] == 1:
                                                            cnt = 0
                                                    if cnt == 5:
                                                        check = 1
                                                        print(1)
                                                        if y > j:
                                                            print(i + 1, j + 1)
                                                        elif y < j:
                                                            print(x + 1, y + 1)
                                                        else:
                                                            if x > i:
                                                                print(i + 1, j + 1)
                                                            elif x < i:
                                                                print(x + 1, y + 1)
                                                        break
                                                    else:
                                                        break
                                                else:
                                                    cnt = 0
                                        else:
                                            cnt = 0
                                else:
                                    cnt = 0
                        else:
                            cnt = 0
                if check == 1:
                    break
        elif matrix[i][j] == 2:
            for l in range(len(dx)):
                for k in range(len(dx)):
                    x = i + dx[l]  # 정해진 방향으로 일직선으로 있어야기 때문에 한번만
                    y = j + dy[k]
                    if (x >= 0 and y >= 0) and (x <= 18 and y <= 18):
                        if matrix[x][y] == 2:
                            cnt = 2  # cnt 2
                            x += dx[l]
                            y += dy[k]
                            if (x >= 0 and y >= 0) and (x <= 18 and y <= 18):
                                if matrix[x][y] == 2:
                                    cnt += 1  # cnt 3
                                    x += dx[l]
                                    y += dy[k]
                                    if (x >= 0 and y >= 0) and (x <= 18 and y <= 18):
                                        if matrix[x][y] == 2:
                                            cnt += 1  # cnt 4
                                            x += dx[l]
                                            y += dy[k]
                                            if (x >= 0 and y >= 0) and (
                                                x <= 18 and y <= 18
                                            ):
                                                if matrix[x][y] == 2:
                                                    cnt += 1  # cnt 5
                                                    nx = x + dx[l]
                                                    ny = y + dy[k]
                                                    if (
                                                        (
                                                            i - dx[l] >= 0
                                                            and j - dy[k] >= 0
                                                        )
                                                        and (
                                                            i - dx[l] <= 18
                                                            and j - dy[k] <= 18
                                                        )
                                                        and matrix[i - dx[l]][j - dy[k]]
                                                        == 2
                                                    ):
                                                        cnt = 0
                                                    if (nx >= 0 and ny >= 0) and (
                                                        nx <= 18 and ny <= 18
                                                    ):
                                                        if matrix[nx][ny] == 2:
                                                            cnt = 0
                                                    if cnt == 5:
                                                        check = 1
                                                        print(2)
                                                        if y > j:
                                                            print(i + 1, j + 1)
                                                        elif y < j:
                                                            print(x + 1, y + 1)
                                                        else:
                                                            if x > i:
                                                                print(i + 1, j + 1)
                                                            elif x < i:
                                                                print(x + 1, y + 1)
                                                        break
                                                    else:
                                                        break
                                                else:
                                                    cnt = 0
                                        else:
                                            cnt = 0
                                else:
                                    cnt = 0
                        else:
                            cnt = 0
                if check == 1:
                    break
        if check == 1:
            break
    if check == 1:
        break
if check == 0:
    print(0)