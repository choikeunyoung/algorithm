T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    
    min_value = num_list[0]
    max_value = num_list[0]
    
    for j in num_list:
        if j <= min_value:
            min_value = j
        
        if j >= max_value:
            max_value = j
    
    print(f"#{i} {max_value-min_value}")