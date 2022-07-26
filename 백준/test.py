T = int(input())
l = 0
cha = [] # 차를 추가할 리스트
check_list=[] # index를 확인할 리스트 생성
mount_list = list(map(int,input().split())) #input 값 생성
for j in range(0,len(mount_list)-1): # 앞 뒤 수를 비교하는 부분
    if mount_list[j] < mount_list[j+1]:
        pass
    elif mount_list[j] == mount_list[j+1]:
        check_list.append(j)
    else:
        check_list.append(j)

if not check_list:
    print("0")
else:
    check_list.append(j+1)
    for k in check_list:
        cha.append(int(mount_list[k])-int(mount_list[l]))
        l = k+1
    print(max(cha))    