# 테스트 케이스 갯수
N = int(input())
# 갯수만큼 반복문 시행
for _ in range(N):
    # 소인수 분해할 수
    number = int(input())
    # 각각 몇개가 들어있는지 체크할 딕셔너리
    num_dict = {}
    # 시작값 2부터
    check = 2
    # input으로 들어온 값이 1보다 큰경우 계속 반복문
    while number>1:
        # 만약 check로 나누어 떨어질 경우
        if number%check == 0:
            # 딕셔너리에 값이 있는지 확인하고 없으면 추가 있으면 1 증가
            if check in num_dict:
                num_dict[check] += 1
            else:
                num_dict[check] = 1
            # number 값을 check로 나눈 몫을 다시 넣어줌
            number //= check
        # 나누어 떨어지지 않을 경우 check 값을 1증가
        else:
            check += 1
    for k,v in num_dict.items():
        print(k,v)