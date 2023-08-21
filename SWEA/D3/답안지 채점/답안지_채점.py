T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    max_point = 0
    min_point = 10**3
    
    ans_list = list(map(int,input().split()))
    
    user_list = [ list(map(int,input().split())) for _ in range(N)]

    for i in user_list:
        total_point = 0
        check_point = 0
        for j in range(M):
            if i[j] == ans_list[j]:
                if check_point != 0:
                    check_point += 1
                else:
                    check_point = 1
                total_point += check_point
            else:
                check_point = 0

        if total_point < min_point:
            min_point = total_point
        if total_point > max_point:
            max_point = total_point
    print(f"#{tc} {max_point-min_point}")