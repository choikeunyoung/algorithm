N = int(input())

ans_list = []

for _ in range(N):
    # 인풋을 리스트 형태로 받아옴
    answer = list(map(int,input().split()))
    # 인풋 리스트를 리스트에 추가
    ans_list.append(answer)
# 최대 몇개의 나라가 존재하는지 갯수 확인
max_value = max(ans_list[:])
max_value = max_value[0]
# 나라의 갯수만큼 리스트 생성하여 메달을 몇개 보유한지 확인
cont_list = [0]*max_value
# 리스트를 점수순으로 정렬
ans_list.sort(reverse=True,key=lambda x : x[:][2])

reword_list = []

for i in ans_list:
    # 상받을 사람이 3명이면 반복문 탈출
    if len(reword_list) == 3:
        break
    # 상받을 사람들 리스트 생성
    else:
        # 그 나라의 메달의 갯수가 2개 미만일 경우 메달갯수를 1더해주고 상리스트에 추가
        if cont_list[i[0]-1] < 2:
            cont_list[i[0]-1] += 1
            reword_list.append([i[0],i[1]])

for j in reword_list:
    print(*j)