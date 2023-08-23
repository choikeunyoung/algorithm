import copy
from pprint import pprint
# 현재 위치, 보는 방향, 좌표
def start_pos(pos, current_dir, matrix_2):
    # 현재 위치 받아오고
    current_pos = pos
    # 현재 보는 방향이 0 위
    if current_dir == 0:
        # 4방향 탐색 진행
        for p in range(4):
            y = current_pos[0] + direction_list[p][0]
            x = current_pos[1] + direction_list[p][1]
            # 범위내에 있는 경우
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                # 그 좌표값이 1과 2가 아니면 => 0 혹은 3이기 때문에
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    # 이동가능하다 판단해서 좌표를 current_pos 값으로 저장
                    current_pos = [y,x]
                    # 보는 방향에 따라서 우측값이 달라지기 때문에 이동한 방향으로 변환
                    if p == 0:
                        p = 1
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 3
                    elif p == 3:
                        p = 2
                    # 이동한 좌표와 보고있는 방향 반환
                    return current_pos, (current_dir + p) % 4
        # 이동 가능한 경우가 없으면 들어온 값 그대로 리턴
        else:
            return current_pos, current_dir
    # 보는 방향 1 오른쪽
    elif current_dir == 1:
        for p in range(4):
            y = current_pos[0] + direction_list_R[p][0]
            x = current_pos[1] + direction_list_R[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    # 이동가능하다 판단해서 좌표를 current_pos 값으로 저장
                    current_pos = [y,x]
                    if p == 0:
                        p = 1
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 3
                    elif p == 3:
                        p = 2
                    # 이동한 좌표와 보고있는 방향 반환
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
    # 보는 방향 2 아래
    elif current_dir == 2:
        for p in range(4):
            y = current_pos[0] + direction_list_D[p][0]
            x = current_pos[1] + direction_list_D[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    # 이동가능하다 판단해서 좌표를 current_pos 값으로 저장
                    current_pos = [y,x]
                    if p == 0:
                        p = 1
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 3
                    elif p == 3:
                        p = 2
                    # 이동한 좌표와 보고있는 방향 반환
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
    # 보는 방향 3 왼쪽
    elif current_dir == 3:
        for p in range(4):
            y = current_pos[0] + direction_list_L[p][0]
            x = current_pos[1] + direction_list_L[p][1]
            if ( 0 <= x < N ) and ( 0 <= y < N ):
                if matrix_2[y][x] != 1 and matrix_2[y][x] != 2:
                    # 이동가능하다 판단해서 좌표를 current_pos 값으로 저장
                    current_pos = [y,x]
                    if p == 0:
                        p = 1
                    elif p == 1:
                        p = 0
                    elif p == 2:
                        p = 3
                    elif p == 3:
                        p = 2
                    # 이동한 좌표와 보고있는 방향 반환
                    return current_pos, (current_dir + p) % 4
        else:
            return current_pos, current_dir
# i,j 좌표에서 방향, 시작 바라보는 위치 설정  
def check_possible(dir, base_direction):
    current_direction = base_direction # 0 위 / 1 오 / 2 왼 / 3 아
    # 각 좌표에서 함수를 복사해와 시뮬레이션 시행
    matrix_2 = copy.deepcopy(matrix)
    # 현재 위치 설정
    current_pos = dir
    # 씨앗 심는 좌표와 요일 설정
    check_day = []
    # 수확의 갯수 체크
    cnt = 0
    # 1일부터 M일까지 반복
    for l in range(1, M+1):
        # 만약 씨앗이 심어져있다면 
        if check_day:
            # 요일 - 심었던 요일 차가 5일인 경우
            if l - check_day[0][-1] == 5:
                # 하루에 씨앗을 한개만 심을수 있기때문에 0 번값을 뺌
                change = check_day.pop(0)
                # 뽑은 값의 좌표가 2인 경우 3으로 변환
                if matrix_2[change[0]][change[1]] == 2:
                    matrix_2[change[0]][change[1]] = 3
        # 이동 가능한 방향을 탐색하는 함수
        current_pos_check, current_direction = start_pos(current_pos, current_direction, matrix_2)

        # 다음으로 이동이 가능할 경우 => 이동 가능하면 좌표값이 다르기 때문에    
        if current_pos != current_pos_check:
            # 만약 현재 위치가 0인 경우
            if matrix_2[current_pos[0]][current_pos[1]] == 0:
                # 현재 위치에 농작물 심어줌
                matrix_2[current_pos[0]][current_pos[1]] = 2
                # 씨앗을 심어줌
                check_day.append([current_pos[0], current_pos[1], l])
            # 만약 현재 위치가 3인 경우
            elif matrix_2[current_pos[0]][current_pos[1]] == 3:
                # 현재 위치 값을 0 으로 변환 후 cnt 증가
                    matrix_2[current_pos[0]][current_pos[1]] = 0
                    cnt += 1
            # 현재위치 갱신
            current_pos = current_pos_check
        else:
            # 갈 수없는 경우 현재 위치가 수확 가능하면 0으로 변환후 cnt 증가
            if matrix_2[current_pos[0]][current_pos[1]] == 3:
                    matrix_2[current_pos[0]][current_pos[1]] = 0
                    cnt += 1
    return cnt

T = int(input())
# 1 산
# 2 벼
# 3 완료
for tc in range(1, T+1):
    direction_list = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction_list_R = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_list_D = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_list_L = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    answer_cnt = 0
    for i in range(N):
        for j in range(N):
            ans = []
            if matrix[i][j] == 0:
                # 현재 바라보는 방향이 0, 1, 2, 3 으로 설정하여 각각 cnt 값을 리스트로 저장해 max 값 반환
                ans.append(check_possible([i,j],0))
                ans.append(check_possible([i,j],1))
                ans.append(check_possible([i,j],2))
                ans.append(check_possible([i,j],3))
                print(ans, i, j)
                if max(ans) > answer_cnt:
                    answer_cnt = max(ans)
    print(f"#{tc} {answer_cnt}")
    
    
    # 이동 후 시작할때 작물심기로 수정