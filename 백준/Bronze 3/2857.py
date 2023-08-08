name_dict = {}
cnt_list = []
for i in range(1,6):
    names = input()
    if 'FBI' in names:
        cnt_list.append(i)
cnt_list.sort()
if cnt_list:    
    for k in cnt_list:
        print(k, end=' ')
else:
    print('HE GOT AWAY!')