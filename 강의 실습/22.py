from pprint import pprint
n,m = list(map(int,input().split()))
nodes = [list(map(int,input().split())) for _ in range(m)]

dict = {}

matrix = [['0' for __ in range(n+1)] for _ in range(n+1)]

for i in nodes:
    matrix[i[0]][i[1]] = '1'
    matrix[i[1]][i[0]] = '1'
pprint(matrix)

adjec = [[] for _ in range(n+1)]

for j in range(len(matrix)):
    cnt = 0
    for k in range(len(matrix)):
        if matrix[j][k] == '1':
            adjec[j].append(k)
print(adjec)
        