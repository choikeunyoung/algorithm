T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 리스트 범위 받아옴
    matrix = [ list(map(int,input().split())) for _ in range(N+1) ]
    # 제일 먼 거리를 찾는 변수
    max_length = 0
    # 1인 좌표들을 넣어줄 리스트
    one_list = []
    # N+1 까지 리스트가 생성되서 반복문도 N+1 까지
    for i in range(N+1):
        for j in range(N+1):
            # 2인 경우 check 라는 리스트를 생성해 2의 좌표를 넣어줌
            if matrix[i][j] == 2:
                check = [i,j]
            # 1인 경우 one_list에 i,j 좌표값들을 리스트 형태로추가
            elif matrix[i][j] == 1:
                one_list.append([i,j])
    # one_list 값 한개씩 순회하며
    for i in one_list:
        # D_check 라는 변수를 만들어서
        # D_check => (1의 y좌표 - 2의 y좌표)제곱 + (1의 x좌표 - 2의 y좌표)제곱
        # 두 점사이 거리 구하는 공식
        D_check = (i[0]-check[0])**2 + (i[1]-check[1])**2
        # 두 점사이 거리가 기존에 제일 먼 거리를 체크할 변수랑 크기 비교한 후
        # 거리가 더 긴 경우 구한 값으로 max_length 할당
        if D_check > max_length:
            max_length = D_check
    # 최소 거리가 되는 제곱근 찾기
    ans = 1
    # ans 라는 변수를 제곱한 수가 max_length 보다 작을때 까지 반복
    while ans**2 < max_length:
        # ans +1
        ans += 1
    # 34 라면 최소 6의 제곱 까지 범위를 넓혀야 포함됨
    # = 넣으면 25일때도 반복문 돌아서 6이 출력되기 때문에 < 인 경우까지
    print(f"#{tc} {ans}")