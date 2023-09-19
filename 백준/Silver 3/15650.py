def N_and_M(num):
    if num == M:
        check.sort()
        if check not in answer:
            answer.append(check[:])
        return
    else:
        for i in range(1,N+1):
            if check:
                if i <= check[-1]:
                    continue
                check.append(i)
                N_and_M(num+1)
                check.pop()
            else:
                check.append(i)
                N_and_M(num+1)
                check.pop()


N, M = map(int,input().split())
answer = []
check = []
N_and_M(0)

for i in answer:
    print(*i)