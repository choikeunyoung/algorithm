T = int(input())

for tc in range(1, T+1):
    p, A_search, B_serach = map(int,input().split())
    A_left = 1
    A_right = p
    B_left = 1
    B_right = p
    A_cnt = 0
    B_cnt = 0
    
    while A_left <= A_right:
        A_mid = (A_left + A_right)//2
        if A_mid < A_search:
            A_left = A_mid
        elif A_mid > A_search:
            A_right = A_mid
        else:
            break
        A_cnt += 1
        
    while B_left <= B_right:
        B_mid = (B_left + B_right)//2
        if B_mid < B_serach:
            B_left = B_mid
        elif B_mid > B_serach:
            B_right = B_mid
        else:
            break
        B_cnt += 1
        
    if A_cnt < B_cnt:
        print(f"#{tc} A")
    elif A_cnt > B_cnt:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")