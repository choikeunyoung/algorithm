T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room_list = [0]*401
    students_list = []
    for _ in range(N):
        students_list.append(list(map(int,input().split())))
    
    for i in students_list:
        if i[0] > i[1]:
            for j in range(i[0], i[1]-1, -1):
                room_list[j] += 1
        else:
            for j in range(i[0], i[1]):
                room_list[j] += 1
    
    max_cnt = max(room_list)
    
    print(f"#{tc} {max_cnt}")