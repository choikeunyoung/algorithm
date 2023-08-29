T = int(input())

for tc in range(1, T+1):
    N, R = map(int,input().split())
    food_list = list(map(int,input().split()))
    for i in range(N):
        food_dict = {}
        food_dict[food_list[i]] = 1
        for j in range(1,R+1):
            if food_list[i-j] in food_dict:
                food_dict[food_list[i-j]] += 1
            else:
                food_dict[food_list[i-j]] = 1
            
            if food_list[(i+j)%N] in food_dict:
                food_dict[food_list[(i+j)%N]] += 1
            else:
                food_dict[food_list[(i+j)%N]] = 1
        if max(food_dict.values()) > 2:
            print(f"#{tc} NO")
            break
    else:
        print(f"#{tc} YES")