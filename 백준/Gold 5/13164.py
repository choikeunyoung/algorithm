N, K = map(int,input().split())

num_list = list(map(int,input().split()))

answer = []

for i in range(1,N):
    answer.append(num_list[i] - num_list[i-1])

ans = 0

answer.sort()

for i in range(N-K):
    ans += answer[i]

print(ans)