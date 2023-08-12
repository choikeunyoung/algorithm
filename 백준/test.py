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


# # 사과문제
# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

#     apples_pos = []
#     for i in range(N):
#         for j in range(N):
#             if matrix[i][j] > 0:
#                 apples_pos.append((matrix[i][j], [i, j]))
#     # 1 / 오른쪽 보고있음 , 2 / 아래 , 3 / 왼쪽 , 4 / 위
#     apples_pos.sort(reverse=True)
#     user_direction = 1
#     user_pos = [0, 0]
#     r_cnt = 0

#     while apples_pos:
#         goal = apples_pos.pop()
#         goal = goal[1]
#         while user_pos != goal:
#             if (
#                 (user_pos[0] < goal[0] and user_pos[1] < goal[1])
#                 or (user_pos[0] > goal[0] and user_pos[1] < goal[1])
#                 or (user_pos[0] < goal[0] and user_pos[1] > goal[1])
#                 or (user_pos[0] > goal[0] and user_pos[1] > goal[1])
#             ):
#                 if user_direction == 1:
#                     user_pos[1] += 1
#                 elif user_direction == 2:
#                     user_pos[0] += 1
#                 elif user_direction == 3:
#                     user_pos[1] -= 1
#                 elif user_direction == 4:
#                     user_pos[0] -= 1
#             elif user_pos[0] < goal[0] and user_pos[1] == goal[1]:
#                 if user_direction == 1:
#                     r_cnt += 1
#                     user_direction += 1
#                 elif user_direction == 2:
#                     pass
#                 elif user_direction == 3:
#                     r_cnt += 3
#                     user_direction += 3
#                 elif user_direction == 4:
#                     r_cnt += 2
#                     user_direction += 2
#                 user_pos[0] += goal[0] - user_pos[0]
#             elif user_pos[0] == goal[0] and user_pos[1] < goal[1]:
#                 if user_direction == 1:
#                     pass
#                 elif user_direction == 2:
#                     r_cnt += 3
#                     user_direction += 3
#                 elif user_direction == 3:
#                     r_cnt += 2
#                     user_direction += 2
#                 elif user_direction == 4:
#                     r_cnt += 1
#                     user_direction += 1
#                 user_pos[1] += goal[1] - user_pos[1]
#             elif user_pos[0] > goal[0] and user_pos[1] == goal[1]:
#                 if user_direction == 1:
#                     r_cnt += 3
#                     user_direction += 3
#                 elif user_direction == 2:
#                     r_cnt += 2
#                     user_direction += 2
#                 elif user_direction == 3:
#                     r_cnt += 1
#                     user_direction += 1
#                 elif user_direction == 4:
#                     pass
#                 user_pos[0] += goal[0] - user_pos[0]
#             elif user_pos[0] == goal[0] and user_pos[1] > goal[1]:
#                 if user_direction == 1:
#                     r_cnt += 2
#                     user_direction += 2
#                 elif user_direction == 2:
#                     r_cnt += 1
#                     user_direction += 1
#                 elif user_direction == 3:
#                     pass
#                 elif user_direction == 4:
#                     r_cnt += 3
#                     user_direction += 3
#                 user_pos[1] += goal[1] - user_pos[1]
#             if user_pos[0] < 0:
#                 user_pos[0] = 0
#                 user_direction += 1
#                 r_cnt += 1
#             elif user_pos[1] < 0:
#                 user_pos[1] = 0
#                 user_direction += 1
#                 r_cnt += 1
#             elif user_pos[0] >= N:
#                 user_pos[0] = N - 1
#                 user_direction += 1
#                 r_cnt += 1
#             elif user_pos[1] >= N:
#                 user_pos[1] = N - 1
#                 user_direction += 1
#                 r_cnt += 1
#             if user_direction > 4:
#                 user_direction -= 4
#     print(f"#{tc} {r_cnt}")


# # 문자열 파싱 도둑문제

# words = input()

# answer_list = []
# answer = ""
# num = ""

# for word in words:
#     if word.isdigit():
#         if answer:
#             answer_list.append(answer)
#             answer = ""
#         num += word
#     else:
#         if num:
#             num = str(int(num) + 17)
#             answer_list.append(num)
#             num = ""
#         answer += word
        
#     if len(answer_list) == 2:
#         print("#".join(answer_list))
#         answer_list.clear()
        
# answer_list.append(str(int(num)+17))
# print("#".join(answer_list))

# 연산자 더하기

# word = input()

# answer_list = []

# ans = ""
# last_ope = ""
# for i in word:
#     if i == "+" or i == "-":
#         if answer_list:
#             if last_ope == "+":
#                 answer_list[-1] += int(ans)
#             elif last_ope == "-":
#                 answer_list[-1] -= int(ans)
#         else:
#             answer_list.append(int(ans))
#         last_ope = i
#         ans = ""
#     else:
#         ans += i

# if last_ope == "+":
#     print(answer_list[-1]+int(ans))
# elif last_ope == "-":
#     print(answer_list[-1]-int(ans))

# 괄호 친구들

# words = input()

# answer_list = [0]
# ans = ""

# big_flag= 0
# small_flag = 0

# for word in words:
#     if word == "[":
#         big_flag = 1
#     elif word == "]":
#         answer_list[-1] += int(ans)
#         ans = ""
#         big_flag = 0  
#     elif word == "{":
#         small_flag = 1
#     elif word == "}":
#         answer_list[-1] *= int(ans)
#         ans = ""
#         small_flag = 0
#     if (big_flag == 1 or small_flag == 1) and (word != "[" and word != "{"):
#         ans += word

# print(answer_list[-1])

# 년도 나누기

# days = list(map(str,input().split(".")))

# year_cnt = 0
# month_cnt = 0
# day_cnt = 0

# if days[0].count("X") >= 1:
#     year_cnt += 1

# if days[1].count("X") == 1:
#     month_cnt = 9
# elif days[1].count("X") == 2:
#     month_cnt = 3

# if days[2].count("X") == 1:
#     if len(days[2]) > 1:
#         if days[2][0] == "X":
#             if int(days[2][1]) <= 1:
#                 day_cnt = 3
#             else:
#                 day_cnt = 2
#         else:
#             day_cnt = 10
#     else:
#         day_cnt = 9
# elif days[2].count("X") == 2:
#     day_cnt = 22

# if year_cnt > 0 and month_cnt > 0 and day_cnt > 0:
#     print(year_cnt * day_cnt * month_cnt)
    
# elif year_cnt == 0 and month_cnt > 0 and day_cnt > 0:
#     print(month_cnt * day_cnt)
    
# elif year_cnt > 0 and month_cnt == 0 and day_cnt > 0:
#     print(year_cnt * day_cnt)
    
# elif year_cnt > 0 and month_cnt > 0 and day_cnt == 0:
#     print(year_cnt * month_cnt)
    
# elif year_cnt > 0 and month_cnt == 0 and day_cnt == 0:
#     print(year_cnt)
    
# elif year_cnt == 0 and month_cnt > 0 and day_cnt == 0:
#     print(month_cnt)
    
# elif year_cnt == 0 and month_cnt == 0 and day_cnt > 0:
#     print(day_cnt)
    
# else:
#     print(0)

# 스택

# num_list = [3, 5, 1, 9, 7]

# word = ""

# for _ in range(4):
#     word += input()
    
# for i in word:
#     if i == "R":
#         ans = num_list.pop()
#         num_list.insert(0,ans)
#     elif i == "L":
#         ans = num_list.pop(0)
#         num_list.append(ans)

# print(*num_list)

# 재귀함수

# def binary_change(num):
#     if num == 1:
#         return "1"
#     else:
#         return str(num%2) + binary_change(num//2)

# N = int(input())
# print(int(binary_change(N)[::-1]))

# DFS

# word = list(map(str,input()))

# matrix = [ list(map(int,input().split())) for _ in range(8) ]

# graph = [ [] for _ in range(8) ]

# for i in range(8):
#     for j in range(7,-1,-1):
#         if matrix[i][j] == 1:
#             graph[i].append(j)
# print(graph)
# for k in range(len(graph)):
#     if graph[k]:
#         stack = graph[k]
#         break

# visited = [False] * 8
# ans = word[k:k+1]
# visited[k] = True

# while stack:
#     check = stack.pop()
#     if not visited[check]:
#         visited[check] = True
#         ans += word[check:check+1]
#         stack.extend(graph[check])
# print("".join(ans))

# DFS 기초

# N = int(input())

# matrix = [ list(map(int,input().split())) for _ in range(N) ]

# graph = [[] for _ in range(N)]

# for i in range(N):
#     for j in range(N-1,-1,-1):
#         if matrix[i][j] == 1:
#             graph[i].append(j)
            
# visted = [False] * N

# visted[0] = True

# stack = graph[0]
# print(0, end=" ")
# while stack:
#     check = stack.pop()
#     if not visted[check]:
#         visted[check] = True
#         stack.extend(graph[check])
#         print(check, end=" ")

# N = int(input())
# arr = [ list(map(int,input().split())) for _ in range(N) ]

# def DFS(now):
#     print(now, end=" ")
#     for i in range(N):
#         if arr[now][i] == 1:
#             DFS(i)

# DFS(0)

# # Level 2 도달 시

# N = int(input())

# matrix = [ list(map(int,input().split())) for _ in range(N) ]

# check = [0]
# visited = [False] * N

# def DFS(now):
#     cnt = 0
#     for i in range(N):
#         if matrix[now][i] == 1:
#             check.append(i)
#             DFS(i)
#         else:
#             cnt += 1
#             if len(check) == 3:
#                 print(*check)
#                 check.pop()
#     if cnt < N:
#         check.pop()

# DFS(0)

# # 추적

# def DFS(point, start):
#     if point[start] not in check:
#         if point[start] != -1:
#             check.append(point[start])
#             DFS(point, point[start])
    

# N = int(input())

# evid = [-1, 0, 0, 1, 2, 4, 4]
# timeStamp = [8, 3, 5, 6, 8 ,9, 10]
# check = [N]

# DFS(evid,N)

# check.sort()

# for i in check:
#     if i == 0:
#         print(f"{i}번 index(출발)")
#     else:
#         print(f"{i}번 index({timeStamp[i]}시)")

# 그래프 순회

# N, K = map(int,input().split())
# start = (int(input())-1)

# graph = [[] for _ in range(N)]

# for _ in range(K):
#     nodes = list(map(int,input().split()))
#     graph[nodes[0]-1].append(nodes[1]-1)

# for i in graph:
#     i.sort(reverse=True)

# post_list = []
# post_visited = [False] * N
# pre_list = []
# pre_visited = [False] * N

# def pre_DFS(start):
#     pre_visited[start] = True
#     pre_list.append(start+1)
#     for node in graph[start]:
#         if not pre_visited[node]:
#             pre_DFS(node)
            
# def post_DFS(start):
#     post_visited[start] = True
#     for node in graph[start]:
#         if not post_visited[node]:
#             post_DFS(node)
#     post_list.append(start+1)
    
# pre_DFS(start)
# post_DFS(start)

# print(*pre_list)
# print(*post_list)

# 바이러스

computers = int(input())
total_computers = int(input())

graph = [[0]*computers for _ in range(computers)]

for _ in range(total_computers):
    pairs = list(map(int,input().split()))
    graph[pairs[0]-1][pairs[1]-1] = 1
    graph[pairs[1]-1][pairs[0]-1] = 1

visited = [False] * computers
cnt = 0

def DFS(start):
    global cnt
    if not visited[start]:
        cnt += 1
        visited[start] = True
        for i in range(computers):
            if graph[start][i] == 1:
                DFS(i)
            
DFS(0)

print(cnt - 1)