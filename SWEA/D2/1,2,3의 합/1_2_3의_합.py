DP = [1, 2, 4]
N = int(input())
for i in range(3,N):
    DP.append(DP[i-1]+DP[i-2]+DP[i-3])
print(DP[N-1])