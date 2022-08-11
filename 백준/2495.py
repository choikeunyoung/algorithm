for i in range(3):
    compare = str()
    cnt_list=[]
    char = input()
    for j in char:
        if compare:
            if compare == j:
                cnt+=1
            else:
                cnt=1
            compare = j
            cnt_list.append(cnt)
        else:
            compare = j
            cnt = 1
            cnt_list.append(cnt)
    print(max(cnt_list))