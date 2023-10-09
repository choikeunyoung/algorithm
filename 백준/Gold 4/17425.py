import sys
# 약수 구하는 함수
def divisor():
    # 약수를 저장할 리스트
    num_list = [1] * 1000001
    # 정답을 출력할 리스트
    ans = [0] * 1000001
    # 2부터 1,000,000 까지 반복
    for i in range(2,1000001):
        # i 부터 1,000,000 까지 반복
        for j in range(i ,1000001,i):
            # 각 1씩 저장된 리스트 j 에 i 값을 더해줌
            # i 값을 더하는 이유가 i 의 배수이기 때문에
            num_list[j] += i
    # 저장된 num_list의 i 값과 ans 의 이전값을 더해나감
    for i in range(1,1000001):
        ans[i] += ans[i-1] + num_list[i]

    return ans

input = sys.stdin.readline
answer = divisor()
T = int(input())

for _ in range(T):
    num = int(input())
    print(answer[num])