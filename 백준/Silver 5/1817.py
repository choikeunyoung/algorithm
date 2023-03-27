N,M = map(int,input().split())
# 책이 0개일 경우
if N == 0:
    print(0)
# 그 외의 경우
else:
    # 책 리스트 생성
    book_list = list(map(int,input().split()))
    # 박스 리스트 생성
    box_list = []
    # 책 리스트 순회
    for i in book_list:
        # 만약 박스 길이가 0 인경우 => 시작 한 경우
        if len(box_list) == 0:
            # 박스에 i 값을 넣어준다
            box_list.append(i)
        # 그 외의 경우
        else:
            # 박스의 바로 위 책의 무게랑 i 값이 M보다 큰 경우
            if box_list[-1]+i > M:
                # 새로운 박스를 생성하여 i 추가
                box_list.append(i)
            # 그 외의 경우 이전값에 더해준다
            else:
                box_list[-1] += i
    # 최종적으로 길이 출력
    print(len(box_list))