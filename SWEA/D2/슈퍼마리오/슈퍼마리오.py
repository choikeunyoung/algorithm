N = int(input())

num_list = list(map(int,input().split()))

DP = []

jump = [2, 7]

if num_list[1] > num_list[6]:
    DP.append([num_list[1],1])
elif num_list[1] < num_list[6]:
    DP.append([num_list[6],6])

while DP[-1][1] < N:
    middle_check = []
    for i in jump:
        check = DP[-1][1] + i
        if check < N:
            middle_check.append([num_list[check],i])
    if middle_check:
        if len(middle_check) > 1:
            if middle_check[0][0] > middle_check[1][0]:
                DP.append([middle_check[0][0],DP[-1][-1]+2])
            elif middle_check[0][0] < middle_check[1][0]:
                DP.append([middle_check[1][0],DP[-1][-1]+7])
        else: