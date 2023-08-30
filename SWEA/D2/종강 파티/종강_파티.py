N, M = map(int,input().split())

price_list = []

mart_price = []

for _ in range(M):
    board_set, alone = map(int,input().split())
    if mart_price:
        if alone < mart_price[-1][-1]:
            mart_price[-1][-1] = alone
        
        if board_set < mart_price[-1][0]:
            mart_price[-1][0] = board_set
    else:
        mart_price.append([board_set,alone])

for i in mart_price:
    quot = N//i[0]
    other = N%i[0]
    if i[0] > i[1]*6:
        check_price = i[1]*6
    elif i[0] < i[1]*6:
        check_price = i[0]
    double_price = i[0]*(quot+1)
    last_price = check_price*quot + i[1]*other
    check_price *= quot
print(min(double_price, last_price, check_price))