import sys

input = sys.stdin.readline

N = int(input())

houses = []
# 최소값 저장 변수
result = 10**9
# 집 마다 색에 대한 값
for _ in range(N):
    houses.append(list(map(int,input().split())))
# 빨, 파, 초 선택하는 범위
for i in range(3):
    # dp 값 각각 0번 집 어느 색을 선택한지에 대한 초기화
    dp = [[10**9] * 3 for _ in range(N)]
    # dp 첫 인덱스 값 갱신
    dp[0][i] = houses[0][i]
    # N번 DP 까지 값 갱신
    for j in range(1,N):
        dp[j][0] = min(dp[j-1][1],dp[j-1][2]) + houses[j][0]
        dp[j][1] = min(dp[j-1][0],dp[j-1][2]) + houses[j][1]
        dp[j][2] = min(dp[j-1][0],dp[j-1][1]) + houses[j][2]
    # 결과값 출력할 반복문 => i번 인덱스와 N 번인덱스는 같으면 안되기 때문에 결과값에서 제외
    for k in range(3):
        if k != i:
            result = min(result,dp[N-1][k])
print(result)