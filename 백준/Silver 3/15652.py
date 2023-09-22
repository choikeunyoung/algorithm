def N_and_M(num):
    if num == M:
        print(*ans)
    else:
        for i in range(1, N+1):
            if ans:
                if i >= ans[-1]:
                    ans.append(i)
                    N_and_M(num+1)
                    ans.pop()
            else:
                ans.append(i)
                N_and_M(num+1)
                ans.pop()


N, M = map(int,input().split())
ans = []

N_and_M(0)