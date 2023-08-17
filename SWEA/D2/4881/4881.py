# def backtraking(level, x, y):
#     global MIN, total
#     if level == N:
        
    


# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     MIN = 1000000000
#     matrix = [ list(map(int,input().split())) for _ in range(N) ]
#     ans = []
    
#     for i in range(N):
#         for j in range(N):
#             total = 0
            
#             backtraking()

# 다빈치 코드

# from itertools import permutations

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)

# if arr[-1] < 0:
#     list_1 = arr[:M-1]
#     list_1.append(arr[-1])
#     list_2 = arr[-1:N-M-1:-1]

#     gop_1 = 1
#     gop_2 = 1
#     for i in range(M):
#         gop_1 *= list_1[i]
#         gop_2 *= list_2[i]

#     if gop_1 < gop_2:
#         list_1.sort()
#         print(*list_1)
#     elif gop_1 > gop_2:
#         list_2.sort()
#         print(*list_2)
# else:
#     print(*arr[-1:N-M-1:-1])