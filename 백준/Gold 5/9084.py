import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    # 동전 리스트
    coins = list(map(int,input().split()))
    # 목표 값
    target = int(input())
    # dp 시작
    dp = [0] * (target+1)
    # 0원 만드는건 1가지 방법
    dp[0] = 1
    # coin 개수로 반복문 시작
    for coin in coins:
        # coin 값부터 목표값 + 1 까지 반복
        for i in range(coin, target+1):
            dp[i] += dp[i-coin]
    print(dp[-1])