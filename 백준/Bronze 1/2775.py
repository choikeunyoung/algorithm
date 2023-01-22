# def pos(x,y):
#     apt = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]] + [ [0]*14 for _ in range(14)]
#     for i in range(1,15):
#         for j in range(14):
#             for k in range(j+1):
#                 apt[i][j] += apt[i-1][k]
#     return apt[x][y-1]

# T = int(input())

# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     print(pos(k,n))

T = int(input())

apt = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]] + [ [0]*14 for _ in range(14)]

for i in range(1,15):
    for j in range(14):
        for k in range(j+1):
            apt[i][j] += apt[i-1][k]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])