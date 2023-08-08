martix = [list(map(str,input())) for _ in range(8)]

row_cnt=0
num_cnt = 0
for i in martix:
    cnt = 0
    if row_cnt % 2 == 0:
        for j in i:
            if cnt % 2 == 0:
                if j == 'F':
                    num_cnt+=1
            cnt+=1
    else:
        for j in i:
            if cnt % 2 != 0:
                if j == 'F':
                    num_cnt+=1
            cnt+=1

    row_cnt+=1

print(num_cnt)