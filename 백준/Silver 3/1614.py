# N 값과 check 값으로 몇번째 손가락 몇번째인지 확인
N  = int(input())
check = int(input())
# 만약 첫번째 손가락의 경우
if N == 1:
    # 1부터 시작해서 2,3,4,5,4,3,2 순으로 8번만에 돌아오기 떄문에 8*check 를 해줌
    print(8*check)
# 두번째 손가락의 경우
elif N == 2:
    # check 가 0인경우는 N에서 -1 을 해주면 된다
    if check == 0:
        print(N-1)
    # 이후 check 값이 0이 아닌경우
    else:
        # check 값이 홀수냐 짝수냐에 따라서 오른쪽에서 오는지 왼쪽에서 오는지가 달라진다.
        # 끝과 끝을 제외하고는 왔다가는 것이 아닌 편도로 값을 확인해야기 떄문에 8이 아닌 4의 배수를 조정하는 것이다.
        # 짝수와 홀수의 경우도 나뉘는데 짝수의 경우 왼쪽에서 오는 시작 값이기 때문에 check 값을 그대로 사용하여도 된다.
        # 홀수의 경우 이미 한번 지나간 후 다시 돌아오는 값이기 때문에 check에 +1 을 해준 4의 배수를 다뤄준다.
        # 손가락 위치에 따라서 두번째 손가락은 +- 1을 조작하고 세번째 손가락은 +- 2 네번째 손가락은 +- 3 다섯빼 새끼 손가락은 +4 만 해주면 된다.
        if check % 2 == 0:
            print(4*check+1)
        else:
            print(4*(check+1)-1)
elif N == 3:
    if check == 0:
        print(N-1)
    else:
        if check % 2 == 0:
            print(4*check+2)
        else:
            print(4*(check+1)-2)
elif N == 4:
    if check == 0:
            print(N-1)
    else:
        if check % 2 == 0:
            print(4*check+3)
        else:
            print(4*(check+1)-3)
elif N == 5:
    print(8*check+4)