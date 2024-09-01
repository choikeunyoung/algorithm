N = int(input())
num_list = list(map(int,input().split()))
max_num = max(num_list)

max_num += 1

answer_list = []

while max_num > 1:
    answer_list.append(max_num//2)
    max_num //= 2

answer_list.sort()
print(*answer_list)