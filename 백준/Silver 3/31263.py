N = int(input())

number = input()
# 사람 수 체크
cnt = 0
# 인덱스 접근
index = N-1
# 인덱스 값이 0 보다 크거나 같을때 반복
while index >= 0:
    # 만약 현재 인덱스 -2 값이 0 보다 작은경우 사람 추가 후 탈출
    if index - 2 < 0:
        cnt += 1
        break
    # 현재 인덱스 기준으로 -2 까지 인덱스 값 정수로 변환
    day = int(number[index-2:index+1])
    # 그 정수값이 100보다 작은 경우 즉 010 이런 경우
    if day < 100:
        # 그 정수값의 길이가 한자리인 경우 인덱스 -1 외에는 -2
        if len(str(day)) < 2:
            index -= 1
        else:
            index -= 2
    # 100보다 큰 경우 인덱스 자리가 3자리
    else:
        # 만약 641 복무일수보다 큰 경우
        if day > 641:
            # 현재 일수를 나눠서 그 자리수 체크
            day_str = str(day)
            # 만약 자리수가 한자리면 인덱스 -1 두자리면 -2
            if int(day_str[1:]) < 10:
                index -= 1
            else:
                index -= 2
        # 641 이내의 경우 인덱스 -3
        else:
            index -= 3
    cnt += 1

print(cnt)