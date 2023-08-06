N = int(input())
direction = input()
# 현재 위치를 0,0 으로 기준으로함
current_pos = [0, 0]
# 남쪽을 보고 서있으므로 남쪽을 1로 정함
current_see = 1
# 움직인 방향을 리스트에 저장 초기값으로 현재위치
answer_list = [current_pos[:]]
# 문자들어온 값에 따라 조건 설정
for dir in direction:
    # L => Left 인 경우
    if dir == "L":
        # 현재 바라보는 방향이 1(남) 이면 2(동)
        if current_see == 1:
            current_see = 2
        # 현재 바라보는 방향이 2(동) 이면 4(북)
        elif current_see == 2:
            current_see = 4
        # 현재 바라보는 방향이 3(서) 이면 4(북)
        elif current_see == 3:
            current_see = 1
        # 현재 바라보는 방향이 4(북) 이면 3(서)
        elif current_see == 4:
            current_see = 3
    # R => Right 인 경우도 위와 같이 설정
    elif dir == "R":
        if current_see == 1:
            current_see = 3
        elif current_see == 2:
            current_see = 1
        elif current_see == 3:
            current_see = 4
        elif current_see == 4:
            current_see = 2
    # F => Front 가 들어온 경우 바라보는 방향에 따라서 현재 위치에서 더해주거나 빼줌
    elif dir == "F":
        if current_see == 1:
            current_pos[0] += 1
        elif current_see == 2:
            current_pos[1] += 1
        elif current_see == 3:
            current_pos[1] -= 1
        elif current_see == 4:
            current_pos[0] -= 1
        # 갱신된 현재 위치를 dir_list 라는 새로운 변수를 생성하여 추가해줌 (얕은 복사)
        dir_list = current_pos[:]
        answer_list.append(dir_list)
min_x = 0
max_x = 0
min_y = 0
max_y = 0
# 0,0을 기준으로 잡았기 때문에 최저 값과 최고 값들을 각각 행과 열에서 찾아줌
for i in answer_list:
    if i[0] < min_x:
        min_x = i[0]
    if i[0] > max_x:
        max_x = i[0]
    
    if i[1] < min_y:
        min_y = i[1]
    if i[1] > max_y:
        max_y = i[1]
# answer 리스트에 저장된 x,y 값에서 최저값을 각각 빼줘서 모든 값을 양수로 변경
for i in answer_list:
    i[0] -= min_x
    i[1] -= min_y
# 반복문 길이를 최고값 - 최저값 +1 인덱스까지 반복
for i in range(max_x-min_x + 1):
    for j in range(max_y-min_y + 1):
        # anwer_list 의 값들과 i,j 값을 비교해서 값이 있으면 .을 출력하고 break
        for k in answer_list:
            if k[0] == i and k[1] == j:
                print(".",end="")
                break
        # break 문을 통해서 나온 것이 아니라 모든 탐색이 끝난 후 나왔을 경우 #을 출력
        else:
            print("#",end="")
    print()