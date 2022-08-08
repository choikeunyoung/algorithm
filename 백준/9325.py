T = int(input())

for i in range(T):
    sum_ = []
    s = int(input())
    n = int(input())
    for j in range(n):
        option_ = list(map(int,input().split()))
        option_ = option_[0] * option_[1]
        sum_.append(option_)
    print(s+sum(sum_))