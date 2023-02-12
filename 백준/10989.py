# N = int(input())
# num_list = [0] * 10001
# for _ in range(N):
#     num_list[int(input())] += 1

# for i in range(1,10001):
#     if num_list[i] > 0:
#         for k in range(num_list[i]):
#             print(i)
print(sum(map(int,input().split())))