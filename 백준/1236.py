n,m = map(int,input().split())

matrix = [list(map(str,input())) for _ in range(n)]
cnt = 0
rows = {}
columns = {}

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'X':
            if i in rows:
                del rows[i]
            break
        else:
            rows[i] = 1

for i in range(m):
    for j in range(n):
        if matrix[j][i] == 'X':
            if i in columns:
                del columns[i]
            break
        else:
            columns[i] = 1

total_cnt = 0

if len(rows) == n and len(columns) == m:
    print(max(n,m))
elif len(rows) == 0 and len(columns) == 0:
    print(0)
else:
    print(max(len(rows),len(columns)))