N = input()
# 숫자를 담을 리스트 생성
num_list = []

# 30으로 나눠야기 때문에 3의 배수인지 확인하는 변수 생성
total = 0
# 정답 출력할 문자 변수 선언
ans = ""
# 30의 배수이므로 30보다 작으면 -1 출력
if int(N) < 30:
    print(-1)
else:
# input으로 받은 N 반복문 돌리는 과정
    for i in N:
    # total 이라는 값에 변수 더해나가고 리스트에 값 추가
        total += int(i)
        num_list.append(i)
    # 리스트 값을 내림차순 정렬
    num_list.sort(reverse=True)
    # 30의 배수가 될려면 맨 마지막자리에 0이 들어가야 하므로 조건식 생성
    if num_list[-1] != "0":
        print(-1)
    else:
    # 0이 끝자리에 존재할 경우 3의 배수인지 체크
        if total % 3 != 0:
            print(-1)
        else:
            for k in num_list:
                ans += k
            print(ans)