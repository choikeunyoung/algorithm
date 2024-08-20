N = int(input())

num_list = list(map(int,input().split()))

# 투 포인터
left = 0
right = 0
# 과일 개수 체크
count = [0] * (10)
# 과일 종류
kind = 0
# 리스트 끝에 도달할때까지 반복문 진행
while right < N:
    # 과일의 개수가 0 인 경우 과일 종류 + 1
    if count[num_list[right]] == 0:
        kind += 1
    # 과일의 개수 + 1
    count[num_list[right]] += 1
    # 종류가 2개 넘을 경우
    if kind > 2:
        # 시작 위치의 과일 개수 -1
        count[num_list[left]] -= 1
        # 위의 계산에서 과일의 개수가 0이 됐을 경우 종류 -1
        if count[num_list[left]] == 0:
            kind -= 1
        # 시작 위치 조정
        left += 1
    # right 탐색 변수 1 증가
    right += 1
print(right-left)