# N = int(input())
# # 매트릭스 담을 리스트
# matrix = [list(map(str,input())) for _ in range(N)]
# # 방문했는지 체크 여부
# visited = [[False] * N for _ in range(N) ]
# # 상하좌우 움직임
# dx = [-1,0,0,1]
# dy = [0,-1,1,0]
# # 총 몇개의 집이 존재하는지 저장할 리스트
# total_length = []
# # N*N 행렬이므로 이중 for문 생성
# for i in range(N):
#     for j in range(N):
#         # 각 j for문마다 상하좌우 통해서 같은 1이나오는 구역 체크
#         stack = []
#         # 만약 matrix 값이 "1" 인 경우
#         if matrix[i][j] == "1":
#             # 방문한 적이 없는경우
#             if not visited[i][j]:
#                 # 갯수 변수를 1로 선언해준 후 stack 에 리스트 형태로 추가
#                 cnt = 1
#                 stack.append([i,j])
#                 # stack 값이 없어질 동안 반복문 시행
#                 while stack:
#                     # stack 값을 뽑아서 stack_list 라는 변수에 저장
#                     stack_list = stack.pop()
#                     # 뽑은 값의 인덱스값에 true 처리해서 방문했다고 표시
#                     visited[stack_list[0]][stack_list[1]] = True
#                     # 상하좌우 탐색을 진행하며 0~N 값사이의 x,y 좌표일 경우 와 "1" 인경우이면서 stack에 중복되지 않을 때 stack 이라는 리스트에 추가 후 cnt 값 추가
#                     for k in range(4):
#                         x = stack_list[1] + dx[k]
#                         y = stack_list[0] + dy[k]
#                         if (x >= 0 and x < N) and (y >= 0 and y < N):
#                             if matrix[y][x] == "1":
#                                 if not visited[y][x] and [y,x] not in stack:
#                                     stack.append([y,x])
#                                     cnt += 1
#                 total_length.append(cnt)
# # 총 길이를 출력 후 오름차순 정렬 후 출력
# print(len(total_length))
# total_length.sort()

# for i in total_length:
#     print(i)

# N = int(input())

# matrix = [list(map(str,input())) for _ in range(N)]
# visited = [[False] * N for _ in range(N) ]

# dx = [-1,0,0,1]
# dy = [0,-1,1,0]
# total_length = []

# for i in range(N):
#     for j in range(N):
#         stack = []
#         if matrix[i][j] == "1":
#             if not visited[i][j]:
#                 cnt = 1
#                 stack.append([i,j])
#                 while stack:
#                     stack_list = stack.pop()
#                     visited[stack_list[0]][stack_list[1]] = True
#                     for i in range(4):
#                         x = stack_list[1] + dx[i]
#                         y = stack_list[0] + dy[i]
#                         if (x >= 0 and x < N) and (y >= 0 and y < N):
#                             if matrix[y][x] == "1":
#                                 if not visited[y][x] and [y,x] not in stack:
#                                     stack.append([y,x])
#                                     cnt += 1
#                 total_length.append(cnt)

# print(len(total_length))
# total_length.sort()

# for i in total_length:
#     print(i)

# N = int(input())

# matrix = [ list(map(int,input().split())) for _ in range(N) ]

# K = int(input())

# max_value = 0

# dx = [-1, 1, -1, 1]
# dy = [-1, -1, 1, 1]

# for i in range(N):
#     for j in range(N):
#         total = 0
#         for l in range(1,K+1):
#             for k in range(4):
#                 x = j + dx[k]*l
#                 y = i + dy[k]*l
#                 if ( 0 <= x < N ) and ( 0 <= y < N ):
#                     total += matrix[y][x]
#         if max_value < total:
#             max_value = total
# print(max_value)


# 사과문제
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    apples_pos = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 0:
                apples_pos.append((matrix[i][j], [i, j]))
    # 1 / 오른쪽 보고있음 , 2 / 아래 , 3 / 왼쪽 , 4 / 위
    apples_pos.sort(reverse=True)
    user_direction = 1
    user_pos = [0, 0]
    r_cnt = 0

    while apples_pos:
        goal = apples_pos.pop()
        goal = goal[1]
        while user_pos != goal:
            if (
                (user_pos[0] < goal[0] and user_pos[1] < goal[1])
                or (user_pos[0] > goal[0] and user_pos[1] < goal[1])
                or (user_pos[0] < goal[0] and user_pos[1] > goal[1])
                or (user_pos[0] > goal[0] and user_pos[1] > goal[1])
            ):
                if user_direction == 1:
                    user_pos[1] += 1
                elif user_direction == 2:
                    user_pos[0] += 1
                elif user_direction == 3:
                    user_pos[1] -= 1
                elif user_direction == 4:
                    user_pos[0] -= 1
            elif user_pos[0] < goal[0] and user_pos[1] == goal[1]:
                if user_direction == 1:
                    r_cnt += 1
                    user_direction += 1
                elif user_direction == 2:
                    pass
                elif user_direction == 3:
                    r_cnt += 3
                    user_direction += 3
                elif user_direction == 4:
                    r_cnt += 2
                    user_direction += 2
                user_pos[0] += goal[0] - user_pos[0]
            elif user_pos[0] == goal[0] and user_pos[1] < goal[1]:
                if user_direction == 1:
                    pass
                elif user_direction == 2:
                    r_cnt += 3
                    user_direction += 3
                elif user_direction == 3:
                    r_cnt += 2
                    user_direction += 2
                elif user_direction == 4:
                    r_cnt += 1
                    user_direction += 1
                user_pos[1] += goal[1] - user_pos[1]
            elif user_pos[0] > goal[0] and user_pos[1] == goal[1]:
                if user_direction == 1:
                    r_cnt += 3
                    user_direction += 3
                elif user_direction == 2:
                    r_cnt += 2
                    user_direction += 2
                elif user_direction == 3:
                    r_cnt += 1
                    user_direction += 1
                elif user_direction == 4:
                    pass
                user_pos[0] += goal[0] - user_pos[0]
            elif user_pos[0] == goal[0] and user_pos[1] > goal[1]:
                if user_direction == 1:
                    r_cnt += 2
                    user_direction += 2
                elif user_direction == 2:
                    r_cnt += 1
                    user_direction += 1
                elif user_direction == 3:
                    pass
                elif user_direction == 4:
                    r_cnt += 3
                    user_direction += 3
                user_pos[1] += goal[1] - user_pos[1]
            if user_pos[0] < 0:
                user_pos[0] = 0
                user_direction += 1
                r_cnt += 1
            elif user_pos[1] < 0:
                user_pos[1] = 0
                user_direction += 1
                r_cnt += 1
            elif user_pos[0] >= N:
                user_pos[0] = N - 1
                user_direction += 1
                r_cnt += 1
            elif user_pos[1] >= N:
                user_pos[1] = N - 1
                user_direction += 1
                r_cnt += 1
            if user_direction > 4:
                user_direction -= 4
    print(f"#{tc} {r_cnt}")
