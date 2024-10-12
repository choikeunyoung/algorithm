import sys

input = sys.stdin.readline

N = int(input())

houses = []

colors = [[10**9] * 3 for _ in range(N)]

for _ in range(N):
    houses.append(list(map(int, input().split())))

colors[0][0] = houses[0][0]
colors[0][1] = houses[0][1]
colors[0][2] = houses[0][2]

for i in range(1, N):
    colors[i][0] = min(colors[i - 1][1], colors[i - 1][2]) + houses[i][0]
    colors[i][1] = min(colors[i - 1][0], colors[i - 1][2]) + houses[i][1]
    colors[i][2] = min(colors[i - 1][0], colors[i - 1][1]) + houses[i][2]

print(min(colors[-1]))
