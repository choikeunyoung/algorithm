import sys

input = sys.stdin.readline

N = int(input())

beer = []
for _ in range(N):
    beer.append(int(input()))
# 맥주의 개수가 1인경우
if N == 1:
    print(beer[0])
# 맥주의 개수가 2인 경우
elif N == 2:
    print(beer[1] + beer[0])
# 맥주의 개수다 3개 이상인 경우
else:
    # 초기맥주의 최대값 0, 1 넣기
    dp = [beer[0], beer[1] + beer[0]]
    # 이후 3번째부터 0, 1, 2 맥주의 최대값을 넣은 후 제일 최소값을 뺴주면 최대로 먹을 수 있는 맥주가 된다.
    dp.append(beer[1] + beer[2] + beer[0] - min(beer[1], beer[0], beer[2]))
    # 그 후 인덱스부터 N까지 반복문
    for i in range(3, N):
        # i 번맥주와 그 이전의 맥주 + 그 전전의 맥주를 마신 최대값과 i번 맥주와 그 2전의 맥주의 최대값을 구한 후 한번더 max를 이용하여 직전의 맥주와 최대값을 찾아줌
        dp.append(max(max(beer[i] + beer[i - 1] + dp[i - 3], beer[i] + dp[i - 2]), dp[i - 1]))

    print(max(dp))
