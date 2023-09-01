def DFS(start):
    global cnt
    global answer
    visited[start[0]][start[1]] = True
    n_y = start[0]
    n_x = start[1]
    value_list = []
    pos_list = []
    while cnt < 3:
        if n_x % 2 == 1:
            for k in range(6):
                ny = n_y + even_dir[k][0]
                nx = n_x + even_dir[k][1]
                if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                    if not visited[ny][nx] and matrix[ny][nx]:
                        value_list.append(matrix[ny][nx])
                        pos_list.append((ny,nx))
        else:
            for k in range(6):
                ny = n_y + odd_dir[k][0]
                nx = n_x + odd_dir[k][1]
                if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                    if not visited[ny][nx] and matrix[ny][nx]:
                        value_list.append(matrix[ny][nx])
                        pos_list.append((ny,nx))
        max_value = max(value_list)
        next_pos = value_list.index(max_value)
        next_pos = pos_list[next_pos]
        value_list.remove(max_value)
        pos_list.remove(next_pos)
        n_y = next_pos[0]
        n_x = next_pos[1]
        answer += max_value
        visited[n_y][n_x] = True
        cnt += 1

T = int(input())

odd_dir = [(-1, -1),(-1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
even_dir = [(0, -1), (0, 1), (1, -1), (1, 1), (1, 0), (-1, 0)]

for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    max_answer = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            answer = matrix[i][j]
            visited = [ [False] * M for _ in range(N) ]
            DFS((i,j))
            if max_answer < answer:
                max_answer = answer
    print(f"#{tc} {max_answer}")