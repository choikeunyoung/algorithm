import sys

input = sys.stdin.readline
# 에라토스테네스의 체
def pri_num():
    num_list = [False,False] + [True] * 1000000

    for i in range(2,round(len(num_list)**0.5)):
        if i%2 == 1:
            if num_list[i] == True:
                for j in range(2*i, len(num_list), i):
                    num_list[j] = False
    return num_list
# 소수 구해둠
pri_list = pri_num()
# 반복문을 통해서
while True:
    # N값이 0 올때까지 구함
    ans_num = int(input())
    if ans_num == 0:
        break
    # 0부터 시작해서 소수 판별 시작해서 차가 가장 큰 경우는 값이 작을때
    for i in range(2,ans_num+1):
        # 홀수인 경우
        if i % 2 == 1:
            # ans_num 에서 i 뺀값과 i 값이 소수인 경우 값 출력 후 탈출
            if pri_list[ans_num - i] and pri_list[i]:
                print(ans_num,"=",i,"+",(ans_num-i))
                break
    # 모든 경우가 안맞으면 출력
    else:
        print("Goldbach's conjecture is wrong.")