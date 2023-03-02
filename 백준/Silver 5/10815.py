N = int(input())

have_list = list(map(int,input().split()))

M  = int(input())

check_list = list(map(int,input().split()))
# 가진 카드 리스트 정렬
have_list.sort()
# check할 리스트 값들 한개씩 비교해보기 위한 반복문
for i in check_list:
    # 끝을 N-1 로 반복문 시작시 갱싱
    end = N-1
    # 시작을 0으로 반복문 시작시 갱신
    start = 0
    # 중간값은 시작과 끝을 2로 나눈 몫
    mid = (start+end)//2
    # check를 통해서 있는지 없는지 판단
    check = 0
    # 음수가 되면 리스트 범위를 초과하게됨
    while (end-start >= 0):
        # 만약 mid 값이 원하는 값인 경우 check 에 1을 넣고 break
        if i == have_list[mid]:
            check = 1
            break
        # 만약 i 값이 중간값보다 작은 경우 끝점을 중간값 -1 로 변경
        elif i < have_list[mid]:
            end = mid-1
        # 만약 i 값이 중간값보다 큰 경우 끝점을 중간값 +1 로 변경
        elif i > have_list[mid]:
            start = mid+1
        # 매 반복문 끝마다 중간값 갱신
        mid = (end+start)//2
    # while이 끝날을 때 check 값에 따라 출력
    if check == 0:
        print("0 ", end="")
    else:
        print("1 ", end="")
