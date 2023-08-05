matrix = [ list(map(int,input().split())) for _ in range(5) ]
matrix_2 = [ list(map(int,input().split())) for __ in range(5) ]

bingo_check = [[False] * 5 for _ in range(5) ]
cnt = 0

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for i in range(5):
    for j in range(5):
        cnt += 1
        end = 0
        flag = 0
        for l in range(5):
            for k in range(5):
                if matrix[l][k] == matrix_2[i][j]:
                    bingo_check[l][k] = True
                    flag = 1
                    break
            if flag == 1:
                break

        if cnt >= 12:
            bingo_set = set()
            for l in range(5):
                for k in range(5):
                    if bingo_check[l][k] == True:
                        for m in range(8):
                            answer_list = [matrix[l][k]]
                            check = 1
                            dl = l + dy[m]
                            dk = k + dx[m]
                            if (0 <= dl < 5) and (0 <= dk < 5):
                                while True:
                                    if bingo_check[dl][dk] == True:
                                        check += 1
                                        answer_list.append(matrix[dl][dk])
                                        dl += dy[m]
                                        dk += dx[m]
                                        if (0 <= dl < 5) and (0 <= dk < 5):
                                            pass
                                        else:
                                            break
                                    else:
                                        break

                            if check == 5:
                                answer_list.sort()
                                bingo_set.add(tuple(answer_list))
                                break
                if len(bingo_set) == 3:
                    end = 1
                    break
            if end == 1:
                break
        if end == 1:
            break
    if end == 1:
        print(matrix_2[i][j])
        break