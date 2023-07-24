T = int(input())

for i in range(T):
    # 하루 식사 제한
    day_meal = int(input())
    # 돼지들의 총 식사
    pig_meal = list(map(int,input().split()))
    # 일수
    cnt = 1
    # 만약 초기 값이 하루 식사치를 넘었을 경우
    if sum(pig_meal) > day_meal:
        pass
    # 그 외의 경우
    else:
        # 하루치 식사보다 작거나 같을때까지 반복
        while sum(pig_meal) <= day_meal:
            # 홀수 합
            odd_total = 0
            # 짝수 합
            even_total = 0
            # 짝수 합과 홀수 합을 더하는 식
            for j in range(1,7):
                if j % 2 == 0:
                    even_total += pig_meal[j-1]
                else:
                    odd_total += pig_meal[j-1]
            # 각각의 자리에서 홀수 합과 짝수 합을 더해서 다시 넣음
            for k in range(6):
                if k % 2 == 0:
                    pig_meal[k] += even_total
                else:
                    pig_meal[k] += odd_total
            # 다음날로 넘어가기 때문에 cnt 증가
            cnt += 1
    print(cnt)