import copy
from pprint import pprint

def start_pos(pos, current_dir, matrix_2):
    current_pos = pos[:]
    if current_dir == 0:
        for p in range(4):
            y = current_pos[0] + direction_list[p][0]
            x = current_pos[1] + direction_list[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    current_pos = [y,x]
                    if p == 0:
                        p = 1
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 2
                    elif p == 3:
                        p = 3
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
    elif current_dir == 1:
        for p in range(4):
            y = current_pos[0] + direction_list_R[p][0]
            x = current_pos[1] + direction_list_R[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    current_pos = [y,x]
                    if p == 0:
                        p = 2
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 3
                    elif p == 3:
                        p = 1
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
    elif current_dir == 2:
        for p in range(4):
            y = current_pos[0] + direction_list_L[p][0]
            x = current_pos[1] + direction_list_L[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    current_pos = [y,x]
                    if p == 0:
                        p = 2
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 1
                    elif p == 3:
                        p = 3
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
    elif current_dir == 3:
        for p in range(4):
            y = current_pos[0] + direction_list_D[p][0]
            x = current_pos[1] + direction_list_D[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    current_pos = [y,x]
                    if p == 0:
                        p = 3
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 2
                    elif p == 3:
                        p = 1
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
def check_possible(dir, base_direction):
    current_direction = base_direction
    matrix_2 = copy.deepcopy(matrix)
    matrix_3 = [ [0] * N for _ in range(N) ]
    current_pos = dir
    check_day = []
    cnt = 0

    for l in range(1,M+1):
        if check_day:
            check_day_length = len(check_day)
            for _ in range(check_day_length):
                change = check_day.pop(0)
                change[2] += 1
                if change[2] == (3 + matrix_3[change[0]][change[1]]):
                    matrix_2[change[0]][change[1]] = 3
                else:
                    check_day.append(change)

        current_pos_check, current_direction = start_pos(current_pos, current_direction, matrix_2)

        if current_pos != current_pos_check:
            if matrix_2[current_pos[0]][current_pos[1]] == 0:
                matrix_2[current_pos[0]][current_pos[1]] = 2
                matrix_3[current_pos[0]][current_pos[1]] += 1
                check_day.append([current_pos[0], current_pos[1], -1])
            
        if matrix_2[current_pos[0]][current_pos[1]] == 3:
            matrix_2[current_pos[0]][current_pos[1]] = 0
            cnt += 1
            
        current_pos = current_pos_check

    return cnt

T = int(input())
direction_list = [(0, 1), (-1, 0), (0, -1), (1, 0)]
direction_list_R = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction_list_L = [(-1, 0), (0, -1), (1, 0), (0, 1)]
direction_list_D = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    answer_cnt = 0
    for i in range(N):
        for j in range(N):
            ans = []
            if matrix[i][j] == 0:
            
                ans.append(check_possible([i,j],0))
                ans.append(check_possible([i,j],1))
                ans.append(check_possible([i,j],2))
                ans.append(check_possible([i,j],3))
                if max(ans) > answer_cnt:
                    answer_cnt = max(ans)
    print(f"#{tc} {answer_cnt}")