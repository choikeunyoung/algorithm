N = int(input())
weights = list(map(int,input().split()))
K = int(input())
balls = list(map(int,input().split()))

max_weight = sum(weights)

dp = [[0] * (max_weight+1) for _ in range(N+1)]

dp[0][0] = 1

for i in range(1,N+1):
    current = weights[i-1]
    for j in range(max_weight,-1,-1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            if j + current <= max_weight:
                dp[i][j+current] = 1
            if abs(j-current) <= max_weight:
                dp[i][abs(j-current)] = 1

answer = []

for ball in balls:
    if ball > max_weight:
        answer.append("N")
    else:
        if dp[N][ball] == 1:
            answer.append("Y")
        else:
            answer.append("N")
print(" ".join(answer))