s,k,h = map(int,input().split())
dict = {}
dict['Soongsil'] = s
dict['Korea'] = k
dict['Hanyang'] = h
total = s+k+h
if total < 100:
    for k,v in dict.items():
        if min(dict.values()) == v:
            print(k)
else:
    print('OK')