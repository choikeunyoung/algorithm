# 피보나치 수열구하는 함수
def fibo(num):
    num_list = [0, 1]
    if num < 2:
        return num_list[num]
    else:
        for i in range(2, num + 1):
            num_list.append(num_list[i - 1] + num_list[i - 2])
        return num_list[num]


n = int(input())
print(fibo(n))
