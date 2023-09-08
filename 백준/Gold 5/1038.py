# 문자열 체크하는 함수
def checking(num, M):
    # 글로벌 문자 변수 선언
    global check
    global cnt
    global ans
    # M 의 길이가 1로 끝일때
    if M == 1:
        # 이전의 check 값과 num[0] 값의 크기를 비교해 작으면 cnt += 1
        if check > int(num[0]):
            cnt += 1
        # 외의 경우 ans = 1 반환
        else:
            ans = 1
        return
    # check 값이 비어있는 경우
    if check == "":
        # num[0]의 값을 초기값으로 넣어줌
        check = int(num[0])
        # 1 ~ 끝 까지 M은 문자열 길이로 생각해서 -1 해서 넣어줌
        checking(num[1:], M-1)
    # check에 값이 있는 경우
    else:
        # check 보다 값이 작은 경우 재귀
        if int(num[0]) < check:
            check = int(num[0])
            checking(num[1:], M-1)
        # 외의 경우
        else:
            # ans 에 현재 문자열의 길이 M 넣어줌
            ans = M
            return

N = int(input())
# N 이 10보다 작은 경우 N 출력
if N < 10:
    print(N)
# 외의 경우
else:
    # cnt 초기값 9, number는 10 으로 선언
    cnt = 9
    number = 10
    # 2자리수부터 비교하기 때문에 num_length 2로 선언
    num_length = 2
    # cnt 값이 1,000,000 이하까지
    while cnt <= 10**6:
        # check 값 ""로 초기화
        check = ""
        # ans에 문자열 길이 넣어줌
        ans = len(str(number))
        # ans 값이 num_length 보다 크면 ans 값으로 갱신
        if ans > num_length:
            num_length = ans
        # 함수 실행 => number 문자열, 문자열 길이 인자로 넣어줌
        checking(str(number), ans)
        # 초기값과 같은 경우
        if ans == num_length:
            # cnt 값이 증가했기 때문에 number + 1
            number += 1
        # 초기값과 다른 경우
        else:
            # number 값의 몫의 +1 해서 10**ans 한 값을 넣어줌
            number = (number//(10**ans) + 1) * (10**ans)
        # cnt 값이 N과 같은 경우
        if cnt == N:
            # number 에서 -1 한 값 출력 후 반복문 탈출
            print(number-1)
            break
        # 만약 9 넘어갈 경우 -1 출력
        if num_length > 10:
            print(-1)
            break