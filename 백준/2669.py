import sys

square_list = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(4)]

total_pos = []

for i in square_list:
    print(i)
    for k in range(i[0],i[2]):
        for l in range(i[1],i[3]):
            total_pos.append((k,l))
    print(total_pos)
# print(total_pos)
# print(set(total_pos))
# print(len(set(total_pos)))