import sys

input = sys.stdin.readline

N = int(input())

square_point = set()

min_x = sys.maxsize
max_x = -sys.maxsize
min_y = sys.maxsize
max_y = -sys.maxsize

check_list = []

for _ in range(N):
    point = tuple(map(int,input().split()))
    check_list.append(point)
    if min_x > point[0]:
        min_x = point[0]
    
    if min_y > point[1]:
        min_y = point[1]
    
    if max_x < point[0]:
        max_x = point[0]
    
    if max_y < point[1]:
        max_y = point[1]

for i in range(min_y, max_y+1):
    square_point.add((min_x,i))
    square_point.add((max_x,i))


for i in range(min_x+1, max_x):
    square_point.add((i,min_y))
    square_point.add((i,max_y))

cnt = 0
print(check_list)
for k in square_point:
    if k in check_list:
        cnt += 1

print(cnt)
