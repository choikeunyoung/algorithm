import sys

sys.stdin = open("_파리퇴치.txt")

T = int(sys.stdin.readline())

for i in range(1,T+1):
    n,m=list(map(int,sys.stdin.readline().split()))
    matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    
    x = 0
    a = 0
    b = m
    y = m
    
    totla_sum=[]
    while True:
        sum_ = 0
        for l in range(x,y):
            for k in range(a,b):
                sum_+=matrix[l][k]
        totla_sum.append(sum_)
        if b == n:
            a=0
            b=m
            x+=1
            y+=1
            if y > n:
                print(f"#{i} {max(totla_sum)}")
                break
        a+=1
        b+=1
        