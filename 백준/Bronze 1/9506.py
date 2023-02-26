import sys
# 많은 input 값을 받을때는 input 자체의 시간도 줄일려고 생각했다.
input = sys.stdin.readline

# 몇개의 N이 들어오는지 없고 -1인경우에만 마지막이다.
while True:
    num_list = []
    total = 0
    cnt = 1
    num = int(input())
    check = num
    # 만약 input 이 -1인 경우 브레이크
    if num == -1:
        break
    # 외의 경우 약수 구하기
    else:
        while True:
            # num이 1이거나 cnt가 처음 input 이랑 같은 경우
            if num == 1 or cnt == check:
                # 만약 처음 input 값과 약수를 더한 값이 같은경우
                if check == total:
                    print(check, end=" = ")
                    for i in num_list:
                        if i == num_list[-1]:
                            print(i)
                        else:
                            print(i,end=" + ")
                    break
                else:
                    print(check,"is NOT perfect.")
                    break
            # 약수인 조건
            if num%cnt == 0:
                total += cnt
                num_list.append(cnt)
            cnt += 1