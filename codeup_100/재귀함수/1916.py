def fibo(num):
    if num >= N:
        return DP[num-1]
    else:
        DP[num] = (DP[num-1] + DP[num-2]) % 10009
        return fibo(num+1)

N = int(input())
DP = [1,1] + [0]*(N)
DP[0] = 1
DP[1] = 1

print(fibo(2))
