N,M = map(int,input().split())
# 첫번째 행렬 생성
matrix_1 = []
# 첫번째 행렬 값 입력
for _ in range(N):
    num_list = list(map(int,input().split()))
    matrix_1.append(num_list)

L,K = map(int,input().split())
# 두번째 행렬 생성
matrix_2 = []
# 두번째 행렬 값 입력
for _ in range(L):
    num_list = list(map(int,input().split()))
    matrix_2.append(num_list)
# 행렬 곱셈
for i in range(N):
    for l in range(K):
        total = 0
        for j in range(M):
            total += (matrix_1[i][j]*matrix_2[j][l])
        print(total, end=" ")
    print()