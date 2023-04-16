number = input()
check_length = len(number)
answer_list = []

# 행운의 티켓을 확인할 길이가 홀수인 경우 변수에서 -1 해서 짝수로 만들어준다.
if check_length % 2 == 1:
    check_length -= 1

# 탐색할 길이가 0인 경우 반복문 종료
while check_length > 0:
    # 인풋으로 들어온 길이와 확인할 길이가 같은경우
    if len(number) == check_length:
        # total_1, total_2 라는 변수를 선언하여 왼쪽값과 오른쪽값의 합을 계산
        total_1 = 0
        total_2 = 0
        # 확인할 길이(check_length)//2 를 진행하면 중앙값이 되므로 중앙값을 기준으로 왼쪽 오른쪽을 나눔
        number_1 = number[:check_length//2]
        number_2 = number[check_length//2:]
        # 중앙값 길이만큼 반복문을 통해서 왼쪽값과 오른쪽값의 합을 구함
        for i in range(len(number_1)):
            total_1 += int(number_1[i])
            total_2 += int(number_2[i])
        # 합이 같은경우 행운의 티켓이므로 정답 리스트에 추가
        if total_1 == total_2:
            answer_list.append(check_length)
    # 확인할 길이가 인풋 값과 다른 경우
    else:
        # cnt 라는 변수를 통해서 브루트포스를 진행
        cnt = 0
        # 0부터 check_length 길이만큼 문자를 잘라서 탐색하기위해 반복분을 진행하되 인풋값의 길이와 같으면 종료
        while cnt+check_length <= len(number):
            # 값을 구하는 방식은 위와 동일
            total_1 = 0
            total_2 = 0
            answer = number[cnt:cnt+check_length]
            number_1 = answer[:check_length//2]
            number_2 = answer[check_length//2:]
            for j in range(len(number_1)):
                total_1 += int(number_1[j])
                total_2 += int(number_2[j])
            # 초기값으로 0이 주어지기 때문에 0이 아닌 조건도 추가했음
            if total_1 == total_2 and total_2 != 0 and total_1 != 0:
                answer_list.append(check_length)
            # 반복문이 끝날때마다 인덱스 위치를 변경해야 하기 때문에 +1 해줌
            cnt += 1
    # 모든 반복문이 끝날때마다 check_length 값들을 -2 씩해줌 값이 짝수이기 때문에
    check_length -= 2
# while 문이 끝날경우 answer_list 에 값이 없으면 0 있으면 max 값 출력
if len(answer_list) == 0:
    print(0)
else:
    print(max(answer_list))