T = int(input())

for i in range(1,T+1):
    for j in range(T-i,0,-1):
        print(" ", end="")
    print("*"*i)