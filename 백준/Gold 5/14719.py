# H, W 인풋 처리
H, W = map(int,input().split())
# 빗물의 양 리스트로 저장
rains = list(map(int,input().split()))
# 몇칸이 쌓이는지 저장할 변수
answer = 0
# 1 ~ W-2 까지 반복
for i in range(1,W-1):
    # i 값을 기준으로 왼쪽에서 제일 큰 값 찾기
    left_value = max(rains[:i])
    # i 값을 기준으로 오른쪽에서 제일 큰 값 찾기
    right_value = max(rains[i:])
    # 두 값중 작은 값 찾기
    min_value = min(left_value,right_value)
    # 현재 빗물의 양이 최소 값보다 작은 경우
    if rains[i] < min_value:
        # 빗물 저장 할 변수에 min_value 에서 현재 빗물 값 감소
        answer += min_value - rains[i]
# 정답 출력
print(answer)
