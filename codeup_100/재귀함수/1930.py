def superSum(start,end):
    global total
    if start == 0:
        return total + end
    else:
        total += DP[start]
        return superSum(start+1, end)

while True:
    try:
        N,M = map(int,input().split())
        DP = [0] * (M+1)
        for i in range(M+1):
            DP[i] = i
        print(DP)
        total = 0
        print(superSum(N,M))
    except EOFError:
        break