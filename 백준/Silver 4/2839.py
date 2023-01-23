N = int(input())

# 시간 복잡도를 줄이기 위해 5의 배수일 경우 바로 출력
if N%5 == 0:
    print(N//5)
# 5이하일 경우 3인 경우 바로 1 출력 외에는 -1 출력 되게 시간복잡도 절약
elif N < 5:
    if N == 3:
        print(N//3)
    else:
        print(-1)
else:
# check 라는 변수에 5로 나눈 몫을 넣고 reamin 이라는 변수에 5의 나머지 값을 넣음
    check = N // 5
    remain = N % 5
# 무한반복문을 시행하여 remain 값이 3으로 나누어 떨어지는지 판단함.
    while True:
# 만약 나누어 떨어질 경우 5의 몫 + 3의 몫의 결과값이 정답이 되므로 아래 식 구현
        if remain % 3 == 0:
            print(check + remain//3)
            break
# 그 외의 경우 5로 나눴던 몫의 값을 1씩 감소해가며 최적의 수를 찾기 시작함. 하지만 N보다 커질경우는 탐색할 필요 없으므로 그 경우 break문 생성
        else:
            remain += 5
            check -= 1
            if remain > N:
                print(-1)
                break