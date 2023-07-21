T = int(input())

for i in range(T):
    day_meal = int(input())
    pig_meal = list(map(int,input().split()))
    one_day_meal = sum(pig_meal)
    today = 1
    answer_list = []
    while one_day_meal <= day_meal:
        answer_list.append(pig_meal)
        for j in range(6):
            pig_meal[j] += (answer_list[-1][j-1] + answer_list[-1][j-3])
            if j==5:
                pig_meal[j] += answer_list[-1][0]
            else:
                pig_meal[j] += answer_list[-1][j+1]
        one_day_meal = sum(pig_meal)
        today += 1
    print(today)