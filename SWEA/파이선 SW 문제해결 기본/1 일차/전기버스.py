T = int(input())

for tc in range(1,T+1):
    # 한번충전으로 이동하는 거리, 종점 정거장, 충전기 설치된 정거장갯수
    K,N,M = map(int,input().split())
    # 충전기 정거장간의 거리
    pos = list(map(int,input().split()))
    # 도중에 끝나는지 체크
    flag = 0
    # 처음 충전기 위치를 저장
    char_pos = [pos[0]]
    # 총 몇번 충전하는지 체크
    cnt = 0
    # 각 충전기 정거장 마다 거리 차이를 리스트로 생성
    for i in range(M-1):
        char_pos.append(pos[i+1]-pos[i])
    # 충전기 정거장 거리를 순회하며 한번 연료로 갈 수 있는 정거장 보다 큰 경우 0 출력 후 종료변수 flag에 1 대입
    for k in char_pos:
        if k > K:
            print(f"#{tc} 0")
            flag = 1
    # flag 값이 1이 아닌 경우            
    if flag != 1:
        # 이동한 거리 계산
        total = 0
        # 현재 인덱스 계산
        index = 0
        # 인덱스 값이 끝이 아닌 경우
        while index != M:
            # 이동한 거리에 충전소 사이 거리를 더해줌
            total += char_pos[index]
            # 만약 더해준 거리가 연료로 이동할 수 있는 거리를 넘었을 경우
            if total > K:
                # total 변수에 현재 충전기에서 갈 수 있는 거리를 넣어주고
                total = char_pos[index]
                # cnt 값 1증가
                cnt += 1
            # 만약 같은 경우
            elif total == K:
                # totla 값 0 으로 초기화
                total = 0
                # cnt 값 1증가
                cnt += 1
            # 그 외는 인덱스를 계속 증가
            index += 1
            # 만약 index 값이 반복문 탈출 조건인 M에 도달할 경우
            if index == M:
                # 마지막 정거장에서 마지막 충전소 까지 거리를 계산
                check_pos = N-pos[-1]
                # 만약 위에서 계산한 결과가 연료에서 현재 갈 수 있는 거리를 뺀 값보다 큰 경우
                if check_pos > K - total:
                    # cnt 값 증가
                    cnt += 1
        print(f"#{tc} {cnt}")