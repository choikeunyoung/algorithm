T = int(input())
a_reward = {
    1 : 5000000,
    2 : 3000000,
    3 : 2000000,
    4 : 500000,
    5 : 300000,
    6 : 100000
}

b_reward = {
    1 : 5120000,
    2 : 2560000,
    3 : 1280000,
    4 : 640000,
    5 : 320000
}
for i in range (1,T+1):
    total_pri = 0
    a ,b = map(int,input().split())
    if a> 0 and a < 2:
        total_pri+=a_reward[1]
    elif a < 4:
        total_pri+=a_reward[2]
    elif a < 7:
        total_pri+=a_reward[3]
    elif a < 11:
        total_pri+=a_reward[4]
    elif a < 16:
        total_pri+=a_reward[5]
    elif a < 22:
        total_pri+=a_reward[6]
    else:
        total_pri+=0

    if b > 0 and b < 2:
        total_pri+=b_reward[1]
    elif b < 4:
        total_pri+=b_reward[2]
    elif b < 8:
        total_pri+=b_reward[3]
    elif b < 16:
        total_pri+=b_reward[4]
    elif b < 32:
        total_pri+=b_reward[5]

    print(total_pri)