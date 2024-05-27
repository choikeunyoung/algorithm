import sys

input = sys.stdin.readline
# 입력받을 개수
N = int(input())
# 일수, 시간 저장
work_list = []
# Dynamic Programming 실행
dp = [0] * (N+1)
# 일수, 시간 저장
for _ in range(N):
    work_list.append(list(map(int,input().split())))
# 뒤에서부터 반복문 진행
for i in range(N-1,-1,-1):
    # N 값보다 현재 인덱스 + 일의 기간이 크거나 작을경우
    if i + work_list[i][0] <= N:
        # 인덱스 + 일수 더한 일에 저장된 값 + 현재 비용 과 이전 비용중 큰 값을 채택
        dp[i] = max(dp[i+work_list[i][0]]+work_list[i][1],dp[i+1])
    else:
        # 조건에 맞지 않을경우 이전 비용 값 채택
        dp[i] = dp[i+1]

print(dp[0])