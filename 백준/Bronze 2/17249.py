jab = input()
l_cnt = 0
r_cnt = 0
search_ = jab.find('(')
for i in range(0,search_):
    if jab[i] == '@': 
        l_cnt +=1
for j in range(search_,len(jab)):
    if jab[j] == '@':
        r_cnt +=1
print(l_cnt, r_cnt)