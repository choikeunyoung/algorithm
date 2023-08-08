import sys

T = int(sys.stdin.readline())

# 행 => 사람수
# 열 => 점수
score = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

total_score = [0 for _ in range(T)] # 총 점수 리스트 생성 (사람 수 만큼)

for i in range(3):
    search_ = [] # 인덱스 찾는 리스트 생성
    new_matrix = [0 for _ in range(T)] # 열끼리 비교하기 위한 리스트 생성
    cnt = 0 # 횟수 찾는 값 생성
    for j in range(T):
        if score[j][i] in new_matrix: # score 값이 new_matrix에 있을 경우
            search_.append(new_matrix.index(score[j][i])) # search_ 라는 리스트에 score 중복되는 인덱스 반환 append 사용한 이유는 중복값이 두개일 경우 생각
            new_matrix[j] = 0 # 이미 값이 있는경우니 new_matrix[j] 에는 0을 대입
            cnt += 1 # 횟수 1 증가
            if cnt == T: # 행의 갯수를 다 진행했을 경우
                for x in search_: # 중복이라고 넣어진 인덱스 값들을 0으로 변환
                    new_matrix[x] = 0
        else:
            new_matrix[j] = score[j][i] # new_matrix 에 값이 없는 경우 score 대입
            cnt +=1 # 횟수 증가
            if cnt == T: # 행의 갯수가 다 진행했을 경우
                for x in search_: # 위와 동일
                    new_matrix[x] = 0
    print(new_matrix)   
    for k in range(T): # new_matrix 에 저장된 값들을 total_score 라는 리스트의 값들에 더해줌
        total_score[k] += new_matrix[k]

for l in total_score: # 출력
    print(l)