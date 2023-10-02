def N_and_M(num):
    if len(ans) == M:
        if answer:
            if ans != answer[-1]:
                answer.append(ans[:])
        else:
            answer.append(ans[:])
        return
    else:
        for i in range(N):
            if ans:
                if ans[0] != num_list[i]:
                    ans.append(num_list[i])
                    N_and_M(i)
                    ans.pop()
            else:
                ans.append(num_list[i])
                N_and_M(i)
                ans.pop()




N, M = map(int,input().split())
num_list = list((map(int,input().split())))
num_list.sort()

ans = []
answer = []
N_and_M(0)
print(answer)