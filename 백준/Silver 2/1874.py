import sys

input = sys.stdin.readline

N = int(input())
num_list = []
# 초기값 1
value = 1
# N 만큼 만들고 싶은 리스트 값 추가
for _ in range(N):
    num_list.append(int(input()))
# 값들을 저장할 stack 리스트
stack = []
# 기호를 저장할 answer 리스트
answer = []
# 인덱스 번호
index = 0
# push, pop 이 결국엔 N*2 만큼 반복되야 하기 떄문에 반복문 설정
for i in range(N*2):
    # stack 에 값이 있는 경우
    if stack:
        # stack[-1] 값과 num_list[index] 값이 같은 경우
        if stack[-1] == num_list[index]:
            # answer 에 - 추가
            answer.append("-")
            # stack 에서 값 추출
            stack.pop()
            # index 값 1 증가
            index += 1
        # 외의 경우
        else:
            # value 값이 N보다 커지는 걸 막음
            if value <= N:
                # stack 에 value 추가
                stack.append(value)
                # value 값 1증가
                value += 1
                # answer에 + 추가
                answer.append("+")
    # stack 에 값이 없는 경우
    else:
        # value 가 N보다 작으면
        if value <= N:
            # stack, anwer 에 각각 값 추가 후 1 증가
            stack.append(value)
            value += 1
            answer.append("+")
# 만 약 stack 이 있다면 No 없으면 list 출력
if stack:
    print("NO")
else:
    for j in answer:
        print(j)