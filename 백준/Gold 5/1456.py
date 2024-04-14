# 에라토스 테네스의 체를 end 범위까지 시행
def prime_check(end):
    prime_list = [False, False] + [True]*end

    for i in range(2,int(end**.5)+1):
        if prime_list[i]:
            for j in range(i*2,end+1,i):
                prime_list[j] = False
    return prime_list[:end]
    

start, end = map(int,input().split())
# end 범위를 바꿔주기 위해서 end 값 저장
check_end = end
cnt = 0
# 제곱수의 범위까지 end 이내에 있어야기 떄문에 end 의 sqrt를 해준 값에 +1 을 end 범위로 설정
end = int(end**.5)+1
# 에라토스 테네스의 체를 end 의 sqrt 값을 대입
num_list = prime_check(end)
# end 까지 반복문 진행
for i in range(end):
    # 소수인 경우
    if num_list[i]:
        # index 에 i 값 넣은 수 while 문 돌림
        index = i
        while index <= check_end:
            # N 제곱까지 값을 곱해 나감
            index *= i
            # start 와 check_end 사이 범위인 경우 cnt
            if start <= index <= check_end:
                cnt += 1

print(cnt)