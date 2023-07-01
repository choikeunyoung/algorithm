N, M = map(int, input().split())

T = int(input())

apples = []

for _ in range(T):
    apples.append(int(input()))

apples.sort()
move = 0

for i in range(N):
    cnt = 0
    for j in range(T):
        if apples[j] <= M:
            cnt += 1
        else:
            break
    if cnt == T:
        print(move)
    M
