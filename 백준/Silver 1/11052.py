# i 장을 구매하기 위한 최대값 계산 방법 접근

N = int(input())
# 카드 리스트 저장
card_list = list(map(int,input().split()))
# dp 시작
dp = [0] * (N+1)
# dp[1] 값 card_list[0] 으로 초기화
dp[1] = card_list[0]
# N+1 까지 반복문
for i in range(2,N+1):
    # i 값까지 반복문 시행
    for j in range(1,i+1):
        # i 번 dp 에는 i 번째 카드를 구매하기 위해서 최대 값을 갱신해야함
        # i-j 의 경우 dp[i]의 카드를 구매하기 위해 최대값이 들어가있으므로 그 값 + card_list[j-1] 인덱스 값을 더해주면 dp[i] 에 저장된 값과 max 값을 비교하여 갱신해줌
        dp[i] = max(dp[i-j] + card_list[j-1], dp[i])

print(dp[-1])