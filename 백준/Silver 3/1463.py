def answer(num):
    # 0, 1 인 경우는 count 되는 값이 없어서 0
    # 2, 3 인 경우는 한번씩 나누는 값 1이다.
    # 외의 10^6 까지 값이 존재하므로 10^6+1 갯수 리스트 생성
    num_list = [0,0,1,1] + [0]*(10**6-2)
    # 4부터 시작하는 반복문 생셩
    for i in range(4, 10**6+1):
        # 6의 배수인 경우 2로 나눈 값과 3으로 나눴을 때 값을 비교해서 작은 값을 넣어준다.
        if i % 3 == 0 and i % 2 == 0:
            num_list[i] = min(num_list[i // 3]+1,num_list[i // 2]+1)
        # 그 외의 경우
        else:
            # 3으로 나눠지면 i//3 의 인덱스 값을 가져와서 + 1 한 값과 바로 직전의 값에서 + 1 해준 값의 대소를 비교
            if i % 3 == 0:
                num_list[i] = min(num_list[i // 3]+1,num_list[i-1] + 1)
            # 2으로 나눠지면 i//2 의 인덱스 값을 가져와서 + 1 한 값과 바로 직전의 값에서 + 1 해준 값의 대소를 비교
            elif i % 2 == 0:
                num_list[i] = min(num_list[i // 2]+1,num_list[i-1] + 1)
            # 그 외의 경우는 -1 되는 경우밖에 없기 떄문에 직전의 값에서 +1 을 해준다.
            else:
                num_list[i] = (num_list[i-1] + 1)
    return num_list[num]
N = int(input())

print(answer(N))