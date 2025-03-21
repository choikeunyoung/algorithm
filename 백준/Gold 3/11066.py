import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    K = int(input())
    num_list = list(map(int,input().split()))
    pre_sum = [0] * (K+1)
    for index in range(1,K+1):
        pre_sum[index] = pre_sum[index-1] + num_list[index-1]
    
    dp = [[0] * K for _ in range(K)]

    for i in range(1,K): # 파일 간격
        for start in range(K-i): # 시작 위치
            end = start + i # 끝 위치
            dp[start][end] = 10**9

            for current in range(start,end):
                cost = dp[start][current] + dp[current+1][end] + (pre_sum[end + 1] - pre_sum[start])
                dp[start][end] = min(dp[start][end],cost)
    print(dp[0])
    print(dp[0][-1])



# start end	dp[start][end] 최소 비용 계산
# 0	1	40 + 30 = 70
# 1	2	30 + 30 = 60
# 2	3	30 + 50 = 80
# 0	2	70 + 100, 60 + 100 = 160
# 1	3	60 + 110 , 80 + 110 = 170
# 0	3	160 + 170 + (40+30+30+50) = 300