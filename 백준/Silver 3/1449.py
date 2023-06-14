N,L = map(int,input().split())
# 테이프 붙이는 위치
tape_list = list(map(int,input().split()))
# 1000까지 존재하는 테이프 위치
tapes = [0]*1001
# 테이프를 붙인 위치 표시
for i in tape_list:
    tapes[i] = 1
# 테이프가 붙었을때 어디까지 붙여지는지 확인할 리스트
water = [0]*1001
# 테이프 길이가 정렬된 것이 아니기 때문애 정렬
tape_list.sort()
# 테이프 갯수
cnt = 0
# 구멍의 개수 만큼 반복
for i in range(N):
    # 처음 테이프 위치 저장
    tape = tape_list[i]
    # 만약 테이프가 안붙어 있는 경우
    if water[tape] == 0:
        # 테이프를 붙이고
        water[tape] = 1
        # 테이프 길이 만큼 반복문 시행
        for j in range(1,L):
            # 1씩 증가해 가며 1000을 넘으면 중지
            if tape+j > 1000:
                break
            # 외의 경우 
            else:
                # 연속인지 확인하기 위해서 tape에 j 더했을 때 테이프를 붙여야 하는 곳이면 water에 1을 넣어서 붙였다고 표시
                if tapes[tape+j] == 1:
                    water[tape+j] = 1
        # 테이프 갯수 증가
        cnt += 1
print(cnt)