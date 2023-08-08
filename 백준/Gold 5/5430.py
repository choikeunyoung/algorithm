import sys
from collections import deque
# 많은 인풋 처리
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 명령어로 R or D 가 입력됨
    command = input()
    # N 의 갯수만큼 리스트 인풋
    N = int(input())
    # deque 형태로 리스트 ,을 기준으로 잘라버림
    num_list = deque(map(str,input().strip().split(",")))
    # 리스트에서 불필요한 "[","]" 을따로 처리해줌
    num_list[0] = num_list[0].strip("[")
    num_list[-1] = num_list[-1].strip("]")
    # flag 를 통해서 반복문 종료 시점 알려줌
    flag = 0
    # Reverse 가 되야하는지 아닌지 판단할 변수
    reverse_flag = 0
    # command 에 들어있는 변수를 탐색하며
    for i in command:
        # 만약 R인경우 reverse_flag 값이 0 이면 1로 1이면 0으로 변경
        if i == "R":
            if reverse_flag == 0:
                reverse_flag = 1
            elif reverse_flag == 1:
                reverse_flag = 0
        # D인 경우
        elif i == "D":
            # num_list 가 존재하고 num_list 첫번째 값이 "" 이 아닌 경우
            if num_list and num_list[0] != "":
                # reverse_flag 값이 0 이면 왼쪽 값 추출
                if reverse_flag == 0:
                    num_list.popleft()
                # reverse_flag 값이 1 이면 오른쪽 값 추출
                elif reverse_flag == 1:
                    num_list.pop()
            # 만약 위의 조건식 외의 경우
            else:
                # flag 를 통해서 error 가 생긴 것을 알려주고 break
                flag = 1
                print("error")
                break
    # flag 값이 1이 닌 경우
    if flag == 0:
        # deque로 구성된 값을 리스트로 치환
        num_list = list(num_list)
        # 만약 reverse 가 존재하면 
        if reverse_flag == 1:
            # list 값을 역순 정렬
            num_list = num_list[::-1]
            # join을 사용하여 출력형태 변경
            answer = ",".join(num_list)
            print(f"[{answer}]")
        # reverse 가 없으면
        elif reverse_flag == 0:
            # join을 통해서 출력 형태 변경
            answer = ",".join(num_list)
            print(f"[{answer}]")