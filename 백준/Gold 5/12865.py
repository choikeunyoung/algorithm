N, K = map(int,input().split())

weigth_list = []
value_list = []
dp = []
max_value = 0
for _ in range(N):
    W,V = map(int,input().split())
    if W < K:
        if max_value == 0:
            max_value = V
        else:
            if max_value < V:
                max_value = V
        weigth_list.append(W)
        value_list.append(V)

