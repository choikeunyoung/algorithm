def N_and_M(num):
    if num == M:
        print(*ans)
    else:
        for i in num_list:
            if i not in ans:
                ans.append(i)
                N_and_M(num+1)
                ans.pop()
    
N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
ans = []
N_and_M(0)