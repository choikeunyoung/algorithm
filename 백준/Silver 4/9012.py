T = int(input())

for i in range(1,T+1):
    L_cnt = 0
    R_cnt = 0
    str_ = input().strip()
    for i in str_:
        if i == '(':
            L_cnt += 1
        elif i == ')':
            if L_cnt == 0:
                R_cnt += 1
            else:
                L_cnt -= 1
    if L_cnt == 0 and R_cnt == 0:
        print('YES')
    else:
        print('NO')