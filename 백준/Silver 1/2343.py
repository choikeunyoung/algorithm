N, M = map(int, input().split())

num_list = list(map(int, input().split()))
# 시작 점과 끝점 설정을 블루레이 길이로 설정
start = max(num_list)
end = sum(num_list)
# 이분 탐색
while start <= end:
    middle = (start + end) // 2
    # 블루레이 한개씩 더해가며 값 체크
    value = 0
    # 블루레이 개수 체크
    cnt = 1
    for num in num_list:
        # 이전값 + 블루레이 반복문 값이 middle 값보다 작거나 같으면 더하고
        if value + num <= middle:
            value += num
        # 크면 값 갱신 후 블루레이 한개 추가
        else:
            value = num
            cnt += 1
    # 블루레이 개수가 M 보다 작거나 같으면 끝값을 중앙값 -1 로
    if cnt <= M:
        end = middle - 1
    # 외의 경우 시작값 갱신
    else:
        start = middle + 1
# 시작값 출력
print(start)
