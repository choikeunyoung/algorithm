N, M = map(int, input().split())

num_dict = {}
cnt = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i, j) in num_dict:
                num_dict[(i, j)] += 1
            else:
                num_dict[(i, j)] = 1

for v in num_dict.values():
    if v > M:
        cnt += 1
print(cnt)
