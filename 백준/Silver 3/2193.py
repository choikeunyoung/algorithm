def dp(num):
    if num == 1:
        return 1
    else:
        # 실제 값을 구하는 코드
        num_list = [["1"]]
        for _ in range(1,num):
            check_list = []
            for j in num_list[-1]:
                if j[-1] == "1":
                    check_list.append(j+"0")
                else:
                    check_list.append(j+"0")
                    check_list.append(j+"1")
            num_list.append(check_list)
    return len(num_list[num-1])

# 갯수가 피보나치 수열로 증가한다.
def fibo(num):
    num_list = [1,1]
    for i in range(2,num+1):
        num_list.append(num_list[i-2]+num_list[i-1])
    return num_list[num-1]

N = int(input())
print(fibo(N))