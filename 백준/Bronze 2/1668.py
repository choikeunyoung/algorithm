import sys

N = int(input())
reward_list = []
for _ in range(N):
    reward_list.append(int(input()))

cnt = 0
height = -sys.maxsize
for i in reward_list:
    if height < i:
        height = i
        cnt += 1
print(cnt)
cnt = 0
height = -sys.maxsize
for j in reward_list[::-1]:
    if height < j:
        height = j
        cnt += 1
print(cnt)