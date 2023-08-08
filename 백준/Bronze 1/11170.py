T = int(input())

for i in range(T):
    cnt = 0
    num_ = list(map(str,input().split()))
    for j in range(int(num_[0]),int(num_[1])+1):
        for k in str(j):
            if k == '0':
                cnt+=1
    print(cnt)