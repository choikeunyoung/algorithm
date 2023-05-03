N = int(input())
# 가격을 저장할 리스트
price_list = []
# 이득을 저장할 리스트
gain_list = []
# 가격을 리스트 형태로 리스트에 저장
for _ in range(N):
    num = list(map(int,input().split()))
    price_list.append(num)
# 리스트를 오름차순 정렬
price_list.sort()
# 안파는 경우를 체크할 변수
check = 0
# N의 길이만큼 반복문 시행
for i in range(len(price_list)):
    # 각 반복문마다 이득을 계산할 변수
    total = 0
    # i번 가격과 i~N까지 배송비를 빼고 이득에 더해가며 총 이득 계산
    for j in range(i,N):
        gain = price_list[i][0] - price_list[j][1]
        # 음수인 경우 안파는게 이득이다.
        if gain <= 0:
            total += 0
        else:
            total += gain
    # 만약 이득이 0 인경우 check라는 변수를 통해서 안파는 것을 체크함
    if total == 0:
        check += 1
    # 총합을 gain_list 라는데 추가함
    gain_list.append(total)
# 제일 높은 이득을 변수로저장
max_value = max(gain_list)
# check 라는 변수를 통해서 아무한테도 안판 것을 확인한 후 다르면 제일 높은 이득이 나온 값을 출력
if check != N:
    for i in range(N):
        if gain_list[i] == max_value:
            print(price_list[i][0])
            break
else:
    print(0)