N,M = map(int,input().split())
print(N,M)

matrix = [ list(map(str, input().split())) for _ in range(M)]

for i in matrix:
    for j in i:
        if j == "W":
            