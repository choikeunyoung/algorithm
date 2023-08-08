import sys

N = int(sys.stdin.readline())

matrix = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]

vertical = 0
horizon = 0
print(matrix)
for i in matrix:
    cnt = 0
    for j in range(len(i)):
        if i[j] == "X":
            if cnt >= 2:
                horizon+=1
                cnt=0
            else:
                cnt=0
        elif j == (len(i)-1):
            cnt+=1
            if cnt >= 2:
                horizon+=1
                cnt=0
        else:
            cnt+=1

for k in range(N):
    cnt = 0
    for l in range(N):
        if matrix[l][k] == "X":
            if cnt >= 2:
                vertical+=1
                cnt=0
            else:
                cnt=0
        elif l == (N-1):
            cnt+=1
            if cnt >= 2:
                vertical+=1
                cnt=0
        else:
            cnt+=1
print(horizon, vertical)

# 5
# ....X
# ..XX.
# .....
# .XX..
# X....