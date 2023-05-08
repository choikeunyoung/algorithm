N,M = map(int,input().split())
# 각 각의 값이 짝수인지 홀수인지에 따라서 끝값이 결정된다.
if N%2 == 0 and M%2 == 0:
    print(min(N,M)//2-1,min(N,M)//2)
elif N%2 == 0 and M%2 != 0:
    if N < M:
        print(N//2-1,N//2)
    else:
        print(N-(M//2)-1,M//2)
elif N%2 != 0 and M%2 == 0:
    if N > M:
        print(M//2-1,M//2)
    else:
        print(N//2,M-(N//2)-1)
else:
    if N == M:
        print(N//2,M//2)
    elif N > M:
        print(N-(M//2)-1, M//2)
    elif N < M:
        print(N//2,M-(N//2)-1)