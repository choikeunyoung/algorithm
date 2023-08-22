def check_possible(dir):
    check_direction = [0, 0, 0, 0] # 오 위 왼 아
    for k in range(4):
        y = dir[0] + direction_list[k]
        x = dir[1] + direction_list[k]
        if ( 0 <= x < N ) and ( 0 <= y < N ):
            if matrix[y][x] != 1 and matrix[y][x] != 2:
                che
        

T = int(input())
# 1 산
# 2 벼
# 3 완료
for tc in range(1, T+1):
    direction_list = [(1,0), (0,-1), (-1,0), (0,1)]
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]