T = int(input())
mes_dict = {}
for i in range(1,T+1):
    mes = input()
    if mes == 'ENTER':
        continue
    else:
        if mes in mes_dict:
            mes_dict[mes] += 1
        else:
            mes_dict[mes] = 1
cnt = 0
for v in mes_dict.values():
    if v == 1:
        cnt +=1
    else:
        continue
print(cnt)