a,b = map(int,input().split())
sum_list=[]
x = 0
y = 0
sum_list.append(a+b)
a = str(a)
b = str(b)
if '5' in a:
    x = a.replace('5','6')
else:
    x = a
if '5' in b:
    y = b.replace('5','6')
else:
    y = b
sum_list.append(int(x)+int(y))

if '6' in a:
    x = a.replace('6','5')
else:
    x = a
if '6' in b:
    y = b.replace('6','5')
else:
    y = b
sum_list.append(int(x)+int(y))
print(min(sum_list), max(sum_list))