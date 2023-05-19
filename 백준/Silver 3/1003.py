def fibonacci():
    # 피보나치 함수에서 각각 0과 1이 나오는 횟수
    num_list = [[1,0],[0,1]]
    # 최대 40 까지 오기 때문에 미리 리스트를 생성해둔다.
    for i in range(2,41):
        num_list.append([num_list[i-1][0]+num_list[i-2][0],num_list[i-1][1]+num_list[i-2][1]])
    return num_list

T = int(input())
# 피보나치 수열 함수 생성
fibo = fibonacci()

for _ in range(T):
    # 미리 생성해둔 함수에서 인풋값에 따라 
    num = int(input())
    print(*fibo[num])