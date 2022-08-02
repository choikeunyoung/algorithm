T = int(input())
l = 0
cha = [] # 차를 추가할 리스트
check_list=[] # index를 확인할 리스트 생성
mount_list = list(map(int,input().split())) #input 값 생성
for j in range(0,len(mount_list)-1): # 앞 뒤 수를 비교하는 부분
    if mount_list[j] < mount_list[j+1]:
        continue
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


N = int(input()) # 8
Pi = list(map(int, input().split())) # [12, 20, 1, 3, 4, 4, 11, 1] 
if N == 1:
    print(0)
else:
    result = [] 
    hight = 0
    for i in range(N-1): 
        if Pi[i] < Pi[i+1]: # 현재 숫자가 다음 숫자보다 작을경우 : 오르막길
            hight += (Pi[i+1] - Pi[i]) # 오르막길에 작은 숫자를 뺀 값 누적 20 - 12 = 8, 3-1 = 2, 4-3=1 = 3, 11-4 = 7 
        else: # 현재 숫자가 다음 숫자보다 크거나 같을때
            result.append(hight) # 현재값 저장 
            hight = 0 # 0으로 초기화 
    result.append(hight)
    if max(result) > 0:
        print(max(result))
    else:
        print(0)