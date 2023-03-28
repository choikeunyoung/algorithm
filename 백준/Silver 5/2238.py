import sys

U,N = map(int,input().split())

people_list = [[] for _ in range(10001)]
cnt_list = [0]*10001
min_value = 10001
for _ in range(N):
    name,price = input().split()
    price = int(price)
    people_list[price].append(name)
    cnt_list[price] += 1

for i in range(len(cnt_list)):
    if cnt_list[i] > 0:
        min_value = min(cnt_list[i],min_value)

for j in range(len(cnt_list)):
    if min_value == cnt_list[j]:
        print(people_list[j][0],j)
        break