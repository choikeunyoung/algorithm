N = int(input())

for _ in range(N):
    mul,hap = map(int,input().split())
    flag = 0
    if mul > 0 and hap > 0 or mul < 0 and hap < 0:
        if hap
        for i in range(1,mul+1):
            if mul % i == 0:
                if hap == ((mul//i) + (i)):
                    flag = 1
                    break
        if flag == 0:
            print("no")
        else:
            print("yes")
    else:
        print("no")