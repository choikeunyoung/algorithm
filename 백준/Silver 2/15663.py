def N_and_M(num):
    if len(ans) == M:
        answer.add(tuple(ans))
        return
    else:
        for i in range(N):
            if i != num:
                if num_dict[num_list[i]] > 0:
                    num_dict[num_list[i]] -= 1
                    ans.append(num_list[i])
                    N_and_M(i)
                    ans.pop()
                    num_dict[num_list[i]] += 1


N, M = map(int,input().split())
num_list = list((map(int,input().split())))
num_list.sort()
num_dict = {}
for i in num_list:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1
ans = []
answer = set()
N_and_M(-1)
answer = list(answer)
answer.sort()
for i in answer:
    print(*i)