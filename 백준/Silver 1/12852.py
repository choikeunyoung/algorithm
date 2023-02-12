def answer(num):
    # 연산 갯수를 돌려줄 리스트 생성
    cnt_list = [0,0,1,1] + [0]*(num-3)
    # 각 연산 마다 무슨 연산을 했는지 체크해주는 리스트 생성
    num_list = ["0","1","2","3"] + [""]*(num-3)
    for i in range(4, num+1):
        # 6의 배수인 경우
        if i % 2 == 0 and i % 3 == 0:
            # 더 작은 값의 연산을 연산 갯수, 무슨 연산 했는지 체크해주는 리스트에 값을 넣음
            if cnt_list[i // 2] + 1 > cnt_list[i // 3] + 1:
                cnt_list[i] = cnt_list[i // 3] + 1
                num_list[i] = num_list[i // 3] + "3"
            else:
                cnt_list[i] = cnt_list[i // 2] + 1
                num_list[i] = num_list[i // 2] + "2"
        else:
            if i % 2 == 0:
                # 더 작은 값의 연산을 연산 갯수, 무슨 연산 했는지 체크해주는 리스트에 값을 넣음
                if cnt_list[i // 2] + 1 > cnt_list[i-1] + 1:
                    cnt_list[i] = cnt_list[i - 1] + 1
                    num_list[i] = num_list[i - 1] + "-"
                else:
                    cnt_list[i] = cnt_list[i // 2] + 1
                    num_list[i] = num_list[i // 2] + "2"
            elif i % 3 == 0:
                # 더 작은 값의 연산을 연산 갯수, 무슨 연산 했는지 체크해주는 리스트에 값을 넣음
                if cnt_list[i // 3] + 1 > cnt_list[i-1] + 1:
                    cnt_list[i] = cnt_list[i - 1] + 1
                    num_list[i] = num_list[i - 1] + "-"
                else:
                    cnt_list[i] = cnt_list[i // 3] + 1
                    num_list[i] = num_list[i // 3] + "3"
            # 모든 2, 3으로 나누는 연산이 안될경우 - 연산자 넣음
            else:
                cnt_list[i] = cnt_list[i - 1] + 1
                num_list[i] = num_list[i - 1] + "-"
        # num 으로 드들어온 list 값반환
    return cnt_list[num],num_list[num]

N = int(input())
# N은 1이상 3이하 값이므로 그 값들은 바로 출력
if N < 4:
    if N == 2:
        print(1)
        print(2, 1)
    elif N == 3:
        print(1)
        print(3, 1)
    else:
        print(0)
        print(1)
# 외의 경우 함수에 값을 넣은 후 리스트를 거꾸로 출력
else:
    ans_list = answer(N)
    print(ans_list[0])
    for i in ans_list[-1][::-1]:
        print(N, end=" ")
        if i == "-":
            N -= 1
        elif i == "2":
            N //= 2
        else:
            N //= 3
    print(1)