# N 보다 커지는 경우의 값과 커지기 직전의 값을 찾는 함수
def make_perm(num):
    # ans_cnt 로 리스트 길이 체크
    global ans_cnt
    # 리스트 길이가 2인 경우 함수 탈출
    if ans_cnt == 2:
        return
    # num 매개변수가 N_length 와 같으면 문자열을 합쳐서 정수로 바꿔 서 answer 리스트에 추가
    if num == N_length:
        checking = int("".join(ans))
        # checking 값이 N 기준값보다 큰 경우
        if checking >= N:
            answer.append(checking)
            ans_cnt += 1
        # checking 값이 N 기준값보다 작은 경우
        else:
            # 만약 answer 리스트가 있으면
            if answer:
                # answer 리스트 값을 뽑아낸다.
                ans_cnt -= 1
                answer.pop()
            # answer 리스트에 값 추가
            ans_cnt += 1
            answer.append(checking)
        return
    else:
        # ans라는 임시 리스트를 통해서 값을 저장 백트래킹
        for i in range(check_length):
            ans.append(check_num[i])
            make_perm(num+1)
            ans.pop()

# N 값을 문자열로 받은 후 길이 저장 후 정수형 변환
N = input()
N_length = len(N)
N = int(N)
# 금지되는 숫자의 갯수
cnt = int(input())
if cnt != 0:
    num_list = list(map(int,input().split()))
# 현재 채널은 100
current = 100
# 현재 채널과 N 값이 같으면 0
if current == N:
    print(0)
# 다를 경우
else:
    # 금지되는 숫자의 개수가 없는 경우 N-current 값과 N_length 값을 비교해서 더 작은 값 출력
    if cnt == 0:
        print(min(abs(N-current),N_length))
    # 외의 경우
    else:
        # check_num 이라는 리스트를생성
        check_num = []
        # ans 리스트 길이 변수
        ans_cnt = 0
        # 사용 가능한 숫자 리스트 생성
        for i in range(10):
            if i not in num_list:
                check_num.append(str(i))
        # 사용 가능한 리스트 길이를 담을 변수
        check_length = len(check_num)
        # 가능한 숫자들로 값을 만들 리스트 생성
        ans = []
        # 조건에 부합하는 값들을 저장할 리스트
        answer = []
        # 사용 가능한 숫자들이 있는 경우
        if check_num:
            # 함수 실행
            make_perm(0)
            # 최소값 비교를 위한 초기 변수
            min_value = 10**9
            # 리스트에 저장된 값을 반복하며
            for j in answer:
                # N값과 리스트에 저장된 값을 저장하여
                number = abs(N-j)
                # min_value 값과 비교한 후
                if number < min_value:
                    min_value = number
            # 저장된 min_value 값과 그 숫자를 누르기 위한 횟수를 더해줌
            min_value += N_length
            # number 라는 빈 문자열 선언
            number = ""
            # N_length 값보다 작은 숫자에서 접근하는 방식이 더 가까울 수 있기 때문에 N_length - 1 까지 반복문시행
            for j in range(N_length-1):
                # 사용가능한 숫자의 끝의 값을 더해줌 => 제일 큰 값이기 때문에
                number += check_num[-1]
            # number 값이 있는 경우
            if number != "":
                # number 값을 정수로 치환
                number = int(number)
                # number 과 N 값의 차 + N_length - 1 값이 min_value 값보다 작은 경우 값 갱신
                if N - number + N_length-1 < min_value:
                    min_value = N - number + N_length-1
            # 다시 빈 number 문자열 선언
            number = ""
            # 사용 가능한 숫자의 0번 인덱스 값이 0인 경우
            if check_num[0] == "0":
                # check_num의 길이가 1보다 크고 check_num의 0번 인덱스가 0인 경우 1번 인덱스 값을 number에 넣어줌
                if len(check_num) > 1 and check_num[0] == "0":
                    number += check_num[1]
                for j in range(N_length):
                    number += check_num[0]
            # 사용 가능한 숫자의 0번 인덱스 값이 0이 아닌 경우
            else:
                # N_length + 1 값까지 반복문 시행하며 0번 인덱스 값을 더해줌
                for j in range(N_length+1):
                    number += check_num[0]
            # number 값이 빈칸이 아닌 경우
            if number != "":
                # 정수로 치환
                number = int(number)
                # number가 0이면
                if number == 0:
                    # N에서 number 차이 + 1 값과 min_value 값 비교 후 값 갱신
                    if abs(number - N) + 1 < min_value:
                        min_value = abs(number - N) + 1
                # number가 0이 아니면
                else:
                    # number 값과 N 값의 차이에서 N_length + 1 값을 더해준 값과 min_value 값 비교 후 갱신
                    if abs(number - N) + N_length + 1 < min_value:
                        min_value = abs(number - N) + N_length + 1
            # 모두 계산한 min_value 값과 N-current 값을 비교 후 값 갱신
            if min_value > abs(N-current):
                min_value = abs(N-current)
            print(min_value)
        # 사용 가능한 숫자가 없으면 N-current 값과 current-N 값 중 더 작은 값 갱신
        else:
            print(min(abs(N-current),abs(current-N)))