N = int(input())

# 돈 단위가 1.00$ 달러가아닌 100으로 표현되서 각 돈에 100을 곱한 리스트 생성
money = [25, 10, 5, 1]

for _ in range(N):
    # 들어온 input 돈을 money 리스트를 반복해가며 몫을 출력하고 나머지를 payback 에 넣어줌
    payback = int(input())
    for i in money:
        print(int(payback//i), end=" ")
        payback %= i
    print()