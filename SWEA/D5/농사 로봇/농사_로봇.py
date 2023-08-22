import copy
from pprint import pprint

def check_possible(dir):
    current_direction = 0 # 0 오 / 1 위 / 2 왼 / 3 아
    matrix_2 = copy.deepcopy(matrix)
    current_pos = dir
    check_day = [[dir[0], dir[1], 0]]
    matrix_2[dir[0]][dir[1]] = 2
    cnt = 0
    for l in range(1,M+1):
        move = 0
        flag = 0
        if check_day:
            if l - check_day[0][-1] == 4:
                change = check_day.pop(0)
                if matrix_2[change[0]][change[1]] == 2:
                    matrix_2[change[0]][change[1]] = 3
        # pprint(matrix_2)
        while move < 1:
            if current_direction == 0:
                y = current_pos[0] + direction_list[3][0]
                x = current_pos[1] + direction_list[3][1]
                if ( 0 <= x < N ) and ( 0 <= y < N ):
                    if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                        if matrix_2[y][x] == 3:
                            cnt += 1
                            matrix_2[y][x] = 0
                        elif matrix_2[y][x] == 0:
                            matrix_2[y][x] = 2
                        current_pos = [y,x]
                        move = 1
                    else:
                        current_direction = (current_direction+1) % 4
            elif current_direction == 1:
                y = current_pos[0] + direction_list[2][0]
                x = current_pos[1] + direction_list[2][1]
                if ( 0 <= x < N ) and ( 0 <= y < N ):
                    if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                        if matrix_2[y][x] == 3:
                            cnt += 1
                            matrix_2[y][x] = 0
                        elif matrix_2[y][x] == 0:
                            matrix_2[y][x] = 2
                        current_pos = [y,x]
                        move = 1
                    else:
                        current_direction = (current_direction+1) % 4
            elif current_direction == 2:
                y = current_pos[0] + direction_list[1][0]
                x = current_pos[1] + direction_list[1][1]
                if ( 0 <= x < N ) and ( 0 <= y < N ):
                    if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                        if matrix_2[y][x] == 3:
                            cnt += 1
                            matrix_2[y][x] = 0
                        elif matrix_2[y][x] == 0:
                            matrix_2[y][x] = 2    
                        current_pos = [y,x]
                        move = 1
                    else:
                        current_direction = (current_direction+1) % 4
            elif current_direction == 3:
                y = current_pos[0] + direction_list[0][0]
                x = current_pos[1] + direction_list[0][1]
                if ( 0 <= x < N ) and ( 0 <= y < N ):
                    if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                        if matrix_2[y][x] == 3:
                            cnt += 1
                            matrix_2[y][x] = 0
                        elif matrix_2[y][x] == 0:
                            matrix_2[y][x] = 2
                        current_pos = [y,x]
                        move = 1
                    else:
                        current_direction = (current_direction+1) % 4
            flag += 1
            if flag == 4:
                break
        else:
            check_day.append([y,x,l])
    return cnt

T = int(input())
# 1 산
# 2 벼
# 3 완료
for tc in range(1, T+1):
    direction_list = [(1,0), (0,-1), (-1,0), (0,1)]
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    answer_cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                ans = check_possible([i,j])
                print(ans, i,j)
                if ans > answer_cnt:
                    answer_cnt = ans
    print(f"#{tc} {answer_cnt}")