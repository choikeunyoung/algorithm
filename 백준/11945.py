n,m=map(int,input().split())
matrix = [list(map(int,input())) for _ in range(n)]
new_matrix = [list( 0 for _ in range(m)) for _ in range(n)]

for i in range(n):
    for j in range(m):
        new_matrix[i][m-j-1]=matrix[i][j]
for k in new_matrix:
    for p in k:
        print(p, end='')
    print()