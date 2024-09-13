import sys

input = sys.stdin.readline

n, k = map(int,input().split())

coins = []
# 동전 저장
for _ in range(n):
    coins.append(int(input()))
# 동전 정렬
coins.sort()
# 동전 중복 제거
coins = set(coins)
# 초기 값으로 10**9 설정 => 동전의 개수가 최소로 사용되기 떄문에 0으로 하면 min 값이 변동됨
dp = [10**9] * 100001
# 동전 순회
for coin in coins:
    # coin 위치 동전 사용횟수 1로 초기화
    dp[coin] = 1
    # coin + 1 부터 시작
    for i in range(coin+1,k+1):
        # i-coin 값이 초기값이 아닌경우
        if dp[i-coin] != 10**9:
            # 현재 dp[i] 값과 dp[i-coin] + 1 한값의 min 값 찾기
            dp[i] = min(dp[i],dp[i-coin] + 1)
# 초기값인 경우 -1 외의 경우 k 인덱스 값 출력
if dp[k] == 10**9:
    print(-1)
else:
    print(dp[k])
