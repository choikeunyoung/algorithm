num_,target = list(map(int,input().split()))
cards = list(map(int,input().split()))
total = []
total_2 = 0
for i in range(num_):
    for j in range(i+1,num_):
        for k in range(j+1,num_):
            total_2 = cards[i]+cards[j]+cards[k]
            if total_2 > target:
                pass
            elif total_2 == target:
                print(total_2)
                exit(0)
            else:
                total.append(total_2)
print(max(total))