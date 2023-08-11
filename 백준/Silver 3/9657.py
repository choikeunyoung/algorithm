N = int(input())

DP = [0,1,0,1,1] + [0]*996

if N >= 5:
    for i in range(5,N+1):
        if not DP[i-1]:
            DP[i] = 1
        if not DP[i-3]:
            DP[i] = 1
        if not DP[i-4]:
            DP[i] = 1

if DP[N]:
    print("SK")
else:
    print("CY")