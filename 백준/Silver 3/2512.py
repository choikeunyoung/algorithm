import sys

N = int(input())
# 돈 리스트 받아오기
money_list = list(map(int,input().split()))
# 돈의 총합
total_money = sum(money_list)
# 제일 많은 돈
max_money = max(money_list)
# 제한된 돈
limit_money = int(input())
# 돈의 총합이 제한된 돈보다 작을 경우 max 값 출력
if total_money <= limit_money:
    print(max_money)
else:
    # 최대로 얼마를 넣을 수 있는지 변수로 최소값 저장
    max_answer = -sys.maxsize
    # 최고값일떄의 인덱스
    max_index = 0

    check_list = []
    # 0 ~ 제일 많은 돈까지 check_list에 저장
    for i in range(max_money+1):
        check_list.append(i)
    # check_list 길이 저장
    check_length = len(check_list)
    # 이분탐색을 위한 left, right 값
    left = 0
    right = check_length
    # left 값이 right 값보다 커지면 탈출
    while left <= right:
        # 각 돈에 대해서 얼마만큼 가격이 나오는지
        check_total = 0
        # 중앙값
        middle = (left+right)//2
        # money_list에서 값을 한개씩 순회하며
        for i in money_list:
            # i 값이 정해진 돈의 값보다 작거나 같은경우 check_total에 i 더함
            if i <= check_list[middle]:
                check_total += i
            # 큰 경우 제한된 돈의 값을 더해줌
            else:
                check_total += check_list[middle]
        # 기존에 최대로 제한된 돈과 기준값으로 제한시킨 돈의 총합을 비교하여 작으면 인덱스와 총합 값을 최신화
        if check_total < limit_money:
            left = middle + 1
            if max_answer < check_total:
                max_answer = check_total
                max_index = middle
        # 클 경우 right 값만 조정
        elif check_total > limit_money:
            right = middle - 1
        # 제한된 값과 같을경우 값을 갱신 후 break
        else:
            max_answer = check_total
            max_index = middle
            break
    print(max_index)