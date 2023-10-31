import math

# 숫자를 리스트로 받아옴
nums = list(map(int, input()))
# 리스트 숫자를 합칠 변수
number = ""
# 최소공배수를 구할 변수
answer = 1
# 리스트를 반복해가며 0이 아닌 값들의 최소공배수를 구하고 숫자를 합쳐줌
for i in nums:
    if i != 0:
        answer = math.lcm(answer, i)
    number += str(i)
# 합친 숫자를 정수로 변환
number = int(number)
# 바로 나누어 떨어지는지 확인하기 위한 몫을 구함
answer_check = number // answer
# 바로 나누어 떨어질 경우 바로 출력
if answer_check * answer == number:
    print(number)
# 외의 경우
else:
    # start 변수에 number 숫자를 넣어줌
    start = number
    # 뒤에 숫자를 붙일 길이 체크
    str_length = 1
    # 무한루프 실행
    while True:
        # check 라는 변수에 start 값 + 0 * str_length 를 더붙여줌
        check = int(str(start) + "0" * str_length)
        # 10의 str_length 제곱수 만큼 반복문시행
        for i in range(10**str_length):
            # 만약 나누어 떨어지면 종료
            if check % answer == 0:
                print(check)
                exit()
            # check 값을 1씩 더해나감
            check += 1
        # 반복문 종료하면 0의 길이를 추가
        str_length += 1
