# 연산 결과가 0인 값을 출력할 함수
def calculator(num):
    global ans
    # 연산을 진행할 변수
    answer = ""
    # 정답을 출력할 변수
    temp = ""
    # N값과 num이 같으면
    if num == N:
        # 마지막 값을 리스트에 추가
        ans.append(str(num))
        # ans 값을 순회하며
        for i in ans:
            # 공백인 경우 정답을 출력할 변수에 값을 더해줌
            if i == " ":
                temp += i
            # 외의 경우 둘다 값 추가
            else:
                answer += i
                temp += i
        # 연산한 결과가 0인 경우 temp 출력
        if eval(answer) == 0:
            print(temp)
        # 백트래킹
        ans.pop()
        return
    else:
        # 연산자를 반복하며 재귀와 백트래킹
        for i in [" ","+", "-"]:
            ans.append(str(num))
            ans.append(i)
            calculator(num+1)
            ans.pop()
            ans.pop()
T = int(input())

for _ in range(T):
    N = int(input())
    ans = []
    calculator(1)
    print()