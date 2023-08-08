total = int(input())
items = int(input())
sum_items = 0
for i in range(items):
    price, item = map(int,input().split())
    sum_items += (price*item)
if sum_items == total:
    print('Yes')
else:
    print('No')
