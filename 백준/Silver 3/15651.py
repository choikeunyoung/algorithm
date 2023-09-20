def N_and_M(num):
    if num == M:
        print(*answer)
    else:
        for i in range(1,N+1):
            answer.append(i)
            N_and_M(num+1)
            answer.pop()

N, M = map(int,input().split())
answer = []

N_and_M(0)