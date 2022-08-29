T = int(input())
mes_dict = {}
cnt = 0
for i in range(1,T+1):
    mes = input()
    if mes == 'ENTER':
        mes_dict = {}
    else:
        if mes in mes_dict:
            mes_dict[mes] += 1
        else:
            mes_dict[mes] = 1
            cnt += 1
print(cnt)