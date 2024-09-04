import sys

n, k = map(int,input().split())
# 동전 저장 리스트
coins = []

# 동전 저장
for _ in range(n):
    coins.append(int(input()))
# 동전 정렬
coins.sort()

dp = [0] * (k+1)
# 0원을 만드는 방법도 1개
dp[0] = 1
# 동전 반복 진행
for coin in coins:
    # 초기값 동전부터 1씩 더해나감
    for i in range(coin,k+1):
        # i번째 동전의 경우 i-coin 한 값을 더해나가야함 동전이 계속 값이 바뀌기 때문에
        dp[i] += dp[i-coin]

print(dp[-1])