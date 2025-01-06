N = int(input())

num_list = list(map(int,input().split()))
answer = [0] * N
max_index = 0

for i in range(N):
    answer[i] = num_list[i]
    for j in range(i):
        if num_list[i] > num_list[j]:
            answer[i] = max(answer[i], answer[j]+num_list[i])
print(max(answer))