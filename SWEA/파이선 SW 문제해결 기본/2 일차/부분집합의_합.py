# from itertools import combinations

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# T = int(input())

# for tc in range(1, T + 1):
#     N, K = map(int,input().split())
#     cnt = 0
#     comb_list = list(combinations(num_list,N))
#     for i in comb_list:
#         if sum(i) == K:
#             cnt += 1
    
#     print(f"#{tc} {cnt}")

# 비트연산 풀이
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    cnt = 0
    
    for i in range(1 << 12):
        # 0~4097
        sum_sub = 0
        subset = []
        for j in range(12):
            # i 의 j번째 비트가 1인지 아닌지 알 수 있다.
            # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 -> 0100
            if i & (1 << j):
                sum_sub += num_list[j]
                subset.append(sum_sub)
        
        if len(subset) == N and sum_sub == K:
            print(subset, i,j)
            cnt += 1
    print(f"#{tc} {cnt}")