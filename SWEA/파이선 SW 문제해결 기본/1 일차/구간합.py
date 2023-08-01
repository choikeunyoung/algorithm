T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    num_list = list(map(int,input().split()))
    # min value 값을 구하기 위해서 리스트 전체값을 임시로 넣어줌
    min_total = sum(num_list)
    # max_value 값은 0 부터 시작
    max_total = 0
    # 반복문을 0부터 N-M+1 까지 시행
    for i in range(N-M+1):
        # 각 반복문 마다 중간에 total 값을 저장할 변수 생성
        total = 0
        # i, i+M 까지 반복문 시행
        for j in range(i,i+M):
            # total 값에 더해줌
            total += num_list[j]
        # 만약 min_total 보다 total 이 작으면 값 갱신
        if min_total > total:
            min_total = total
        # 만약 max_total 보다 total 이 크면 값 갱신
        if max_total < total:
            max_total = total
        
    print(f"#{tc} {max_total - min_total}")