from itertools import combinations

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    cnt = 0
    comb_list = list(combinations(num_list,N))
    for i in comb_list:
        if sum(i) == K:
            cnt += 1
    
    print(f"#{tc} {cnt}")