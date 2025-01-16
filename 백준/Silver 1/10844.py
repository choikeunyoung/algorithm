N = int(input())

dp = [9, 17]

for i in range(2, N):
    dp.append(dp[-1] + ((dp[-1] - dp[-2]) * 2 - (i - 1)))

print(dp)
