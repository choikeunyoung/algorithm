# 엘리스 토끼는 목표량을 정해 수학 문제를 열심히 풉니다. 목표량은 정수입니다.

# 내일 풀 수학 문제의 개수는 오늘 푼 문제 개수의 수와 숫자의 구성이 같으면서, 오늘 푼 문제 개수의 수보다 큰 수 중 가장 작은 수입니다.

# 예를 들어, 오늘 67문제를 풀었으면 다음 날 76문제를 풉니다.

# 오늘 푼 문제의 개수를 줬을 때 다음날 풀 문제의 개수를 출력하는 프로그램을 작성하세요.

# 시간 제한: 1초

# 지시사항

# 입력

# 첫 번째 줄에 오늘 푼 문제의 개수인 자연수 N을 입력합니다. 1 ≤ N ≤ 999999

# 정답이 반드시 있는 경우만 입력값으로 주어집니다.

# 출력

# 다음날 풀 문제의 개수를 출력합니다.


def backtracking(length):
    global number_length
    global number
    global min_value
    if length == number_length:
        num = int("".join(num_list))
        if num > int(number):
            if num < min_value:
                min_value = num
        return

    for i in range(number_length):
        if num_dict[number[i]] != 0:
            num_list.append(number[i])
            num_dict[number[i]] -= 1
            backtracking(length + 1)
            num_dict[number[i]] += 1
            num_list.pop()


min_value = 10**9

number = input().strip()
number_length = len(number)
num_list = []
num_dict = {}
for i in number:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

backtracking(0)
print(min_value)
