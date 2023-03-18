import math

T = int(input())

for _ in range(T):
    X,Y = map(int,input().split())
    answer = math.factorial(Y)//(math.factorial(X)*math.factorial(Y-X))
    print(answer)