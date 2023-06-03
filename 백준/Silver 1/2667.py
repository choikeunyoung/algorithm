N = int(input())
# 매트릭스 담을 리스트
matrix = [list(map(str,input())) for _ in range(N)]
# 방문했는지 체크 여부
visited = [[False] * N for _ in range(N) ] 
# 상하좌우 움직임
dx = [-1,0,0,1]
dy = [0,-1,1,0]
# 총 몇개의 집이 존재하는지 저장할 리스트
total_length = []
# N*N 행렬이므로 이중 for문 생성
for i in range(N):
    for j in range(N):
        # 각 j for문마다 상하좌우 통해서 같은 1이나오는 구역 체크
        stack = []
        # 만약 matrix 값이 "1" 인 경우
        if matrix[i][j] == "1":
            # 방문한 적이 없는경우
            if not visited[i][j]:
                # 갯수 변수를 1로 선언해준 후 stack 에 리스트 형태로 추가
                cnt = 1
                stack.append([i,j])
                # stack 값이 없어질 동안 반복문 시행
                while stack:
                    # stack 값을 뽑아서 stack_list 라는 변수에 저장
                    stack_list = stack.pop()
                    # 뽑은 값의 인덱스값에 true 처리해서 방문했다고 표시
                    visited[stack_list[0]][stack_list[1]] = True
                    # 상하좌우 탐색을 진행하며 0~N 값사이의 x,y 좌표일 경우 와 "1" 인경우이면서 stack에 중복되지 않을 때 stack 이라는 리스트에 추가 후 cnt 값 추가
                    for k in range(4):
                        x = stack_list[1] + dx[k]
                        y = stack_list[0] + dy[k]
                        if (x >= 0 and x < N) and (y >= 0 and y < N):
                            if matrix[y][x] == "1":
                                if not visited[y][x] and [y,x] not in stack:
                                    stack.append([y,x])
                                    cnt += 1
                total_length.append(cnt)
# 총 길이를 출력 후 오름차순 정렬 후 출력
print(len(total_length))
total_length.sort()

for i in total_length:
    print(i)