def solution(land):
    horizontal_length = len(land[0])
    vertical_length = len(land)
    visited = [ [False]*horizontal_length for _ in range(vertical_length) ]
    direction = [ (0,-1), (-1,0), (0,1), (1,0) ]
    for i in range(vertical_length):
        for j in range(horizontal_length):
            if land[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                check_list = [(i,j)]
                visited[i][j] = True
                cnt = 1
                while stack:
                    check = stack.pop()
                    check_list.append(check)
                    for k in range(4):
                        ny = check[0] + direction[k][0]
                        nx = check[1] + direction[k][1]
                        if 0 <= ny < vertical_length and 0 <= nx < horizontal_length:
                            if land[ny][nx] == 1 and not visited[ny][nx]:
                                stack.append((ny,nx))
                                visited[ny][nx] = True
                                cnt += 1
                
                for lists in check_list:
                    land[lists[0]][lists[1]] = cnt
    max_cnt = 0
    for j in range(horizontal_length):
        last_value = land[0][j]
        cnt = land[0][j]
        for i in range(1,vertical_length):
            if last_value != land[i][j]:
                cnt += land[i][j]
            last_value = land[i][j]
        if max_cnt < cnt:
            max_cnt = cnt
    
    answer = max_cnt
    return answer