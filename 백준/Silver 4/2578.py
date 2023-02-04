# 내 빙고
my_bingo = [ list(map(str,input().split())) for _ in range(5)]
# 사회자가 부르는 빙고
ans_bingo = [ list(map(str,input().split())) for _ in range(5)]
# bingo 일치하는 값 저장 리스트
bingo_list = [[], [], [], [], []]
# 3줄비공 조건 확인
flag = 0
# 몇번째 숫자인지 체크
cnt = 0

# 정답 리스트를 순회하며 맞는 값들의 인덱스 찾기
for i in ans_bingo:
    for j in i:
        # 매반복문 마다 몇번째 열을 반복중인지 확인하기 위한 변수
        row_cnt = 0
        for k in my_bingo:
        # 빙고 리스트에서 ans_bingo의 값과 같은 값을 찾기
            if j in k:
            # 만약 값이 같으면 리스트에 index 값 추가
                bingo_list[row_cnt].append(k.index(j))
            row_cnt += 1
        # 몇번 반복했는지 횟수 체크
        cnt += 1
        # 최소 12번이상 시행해야 빙고가 3줄나올 수 있음
        if cnt >= 12:
        # bingo 갯수 체크, 각 열 체크변수들 생성
            bingo_cnt = 0
            one_cnt = 0
            two_cnt = 0
            three_cnt = 0
            four_cnt = 0
            five_cnt = 0
        # 빙고 리스트 => 인덱스 리스트 반복문시행
            for x in bingo_list:
            # 가로로 빙고가 있는지 체크
                if len(x) == 5:
                    bingo_cnt += 1
            # 세로로 빙고가 있는지 체크
                for y in x:
                    if y == 0:
                        one_cnt += 1
                    elif y == 1:
                        two_cnt += 1
                    elif y == 2:
                        three_cnt += 1
                    elif y == 3:
                        four_cnt += 1
                    elif y == 4:
                        five_cnt += 1
                if one_cnt == 5:
                    bingo_cnt += 1
                if two_cnt == 5:
                    bingo_cnt += 1
                if three_cnt == 5:
                    bingo_cnt += 1
                if four_cnt == 5:
                    bingo_cnt += 1
                if five_cnt == 5:
                    bingo_cnt += 1
            # 대각선 빙고 체크
            if 4 in bingo_list[0] and 3 in bingo_list[1] and 2 in bingo_list[2] and 1 in bingo_list[3] and 0 in bingo_list[4]:
                bingo_cnt += 1
            if 0 in bingo_list[0] and 1 in bingo_list[1] and 2 in bingo_list[2] and 3 in bingo_list[3] and 4 in bingo_list[4]:
                bingo_cnt += 1
            # 빙고가 3줄 이상일 경우 종료
            if bingo_cnt >= 3:
                    flag = 1
                    break
            if flag == 1:
                break
    if flag == 1:
        print(cnt)
        break