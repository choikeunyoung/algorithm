E,S,M = map(int, input().split())

s = 0
e = 0
m = 0
e_cnt = 0
s_cnt = 0
m_cnt = 0
check_num = 1
total = 0

while True:
    if (e == E) and (s == S) and (m == M):
        print(check_num-1)
        break
    else:
        s = check_num-(28*s_cnt)
        e = check_num-(15*e_cnt)
        m = check_num-(19*m_cnt)
        if e>=15:
            e_cnt += 1
        if s>=28:
            s_cnt += 1
        if m>=19:
            m_cnt += 1
        check_num += 1