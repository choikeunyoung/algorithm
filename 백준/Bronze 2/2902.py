names = list(map(str,input().split('-')))
shorts = str()

for i in names:
    shorts += i[0:1]
print(shorts)