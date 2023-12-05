import sys

input = sys.stdin.readline

N, C, W = map(int, input().split())

wood_list = []

for _ in range(N):
    wood_list.append(int(input()))

wood_list.sort()

max_wood = 0

for i in range(1, wood_list[-1] + 1):
    current_value = 0
    cut_cnt = 0
    for j in wood_list:
        if j > i:
            cut_cnt += j // i
            if j % i == 0:
                cut_cnt -= 1
                current_value += (j // i - 1) * i
            else:
                current_value += (j // i) * i
        elif j == i:
            current_value += i
    current_value -= cut_cnt * C
    if current_value > max_wood:
        print(current_value, i, cut_cnt)
        max_wood = current_value
print(max_wood)

# 자르는 비용이 파는 비용보다 큰 경우 고려해야함
