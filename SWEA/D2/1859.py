from collections import deque
T = int(input())

for i in range(1,T+1):
    total_pay = 0
    N = int(input())
    pay = deque(map(int,input().split()))
    while pay:
        cnt = 0
        sum_pay = 0
        max_val = pay.index(max(pay))

        if max_val == 0:
            pay.popleft()
        else:
            for k in range(max_val):
                cnt += 1
                sum_pay += pay.popleft()
            total_pay += (pay.popleft()*cnt) - sum_pay
    print(f'#{i}', total_pay)