def backtracking(cnt):
    if cnt == N*2:
        print(answer)
        exit()
    if cnt - (answer[-1] + 1) >= 0 and answer[-1] != answer[cnt-answer[-1]+1]:
        return
    print(answer)
    for j in range(1,N+1):
        if num_dict[j] > 0:
            num_dict[j] -= 1
            answer.append(j)
            backtracking(cnt+1)
            answer.pop()
            num_dict[j] += 1


N = int(input())
num_list = list(map(int,input().split()))

num_dict = {}

for i in num_list:
    num_dict[i] = 2

answer = []


for i in range(1,N+1):
    answer = [i]
    num_dict[i] -= 1
    backtracking(0)
    num_dict[i] += 1

