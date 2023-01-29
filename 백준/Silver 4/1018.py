N,M = map(int,input().split())

# input 매트릭스생성
matrix = [list(map(str, input())) for _ in range(N)]
# White 가 먼저 시작되는 매트릭스 생성
white_matrix = [["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"]]
# Black 이 먼저 시작되는 매트릭스 생성
black_matrix = [["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"]]

# 반복문 중간에 break할 flag 선언
flag = 0
# 각 반복마다 cnt 한 갯수 저장 리스트
max_cnt = []
# 반복문을 input 값에서 -7 해준 이유는 리스트가 0부터 시작이기 때문이고 끝까지 갈 필요없이 8구역씩 보기위해서 선언
for l in range(M-7):
    for k in range(N-7):
        # White 먼저 시작했을때 다른 갯수 체크
        white_cnt = 0
        # Black 먼저 시작했을때 다른 갯수 체크
        black_cnt = 0
        # 8X8 배열 탐색이므로 8까지
        for i in range(8):
            for j in range(8):
                # 각각 배열에서 다를경우 count
                if matrix[k+i][l+j] != white_matrix[i][j]:
                    white_cnt += 1
                if matrix[k+i][l+j] != black_matrix[i][j]:
                    black_cnt += 1
        # cnt list에 둘중 최솟값 추가
        max_cnt.append(min(white_cnt,black_cnt))
        # 0이 나올경우 0보다 작은 값이 나올 수 없기때문에 break를 걸어야한다.
        if min(white_cnt,black_cnt) == 0:
            flag = 1
            break
    if flag == 1:
        break
# max_cnt 리스트에서 최솟값 출력
print(min(max_cnt))