N,M = map(int,input().split())
# 가격리스트를 생성
price_list = []
for _ in range(M):
    price_list.append(int(input()))
# 가격리스트 오름차순 정렬
price_list.sort()
# 각 가격대별 최대값 저장
answer = {}
# M번만큼 반복하여
for i in range(M):
    # 0번 인덱스 부터시작해서 M 까지 반복하는데 계란의 갯수가 N개까지 밖에 없기 때문에 변수를 따로 구해준다.
    egg = M-i
    # 만약 달걀의 갯수가 N보다 큰경우 N 으로 바꿔준다.
    if egg > N:
        egg = N
    # 딕셔너리에 각 가격별 최대 값을 저장
    answer[price_list[i]] = price_list[i]*egg
# 최대 값을 변수로 저장
max_value = max(answer.values())
# value 값이 최대값인 경우 가격과 최대값 출력
for k,v in answer.items():
    if v == max_value:
        print(k,v)