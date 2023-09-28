def N_and_M(num):
    if num == M:
        print(*answer)
    else:
        for i in range(1,N+1):
            print(answer)
            answer.append(i)
            N_and_M(num+1)
            answer.pop()
            print(answer)

N, M = map(int,input().split())
answer = []

N_and_M(0)