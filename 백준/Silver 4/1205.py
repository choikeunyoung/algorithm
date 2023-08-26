N,P,limit = map(int,input().split())

if N == 0:
    print(1)
else:
    num_list = list(map(int,input().split()))

    num_list.sort(reverse=True)

    rank_list = []

    for i in num_list:
        if len(rank_list) == limit:
            break
        else:
            rank_list.append(i)
    
    rank_length = len(rank_list)

    if rank_length == limit:
        if rank_list[-1] >= P:
            print(-1)
        else:
            for i,v in enumerate(rank_list):
                if v == P:
                    print(i+1)
                    break
                elif v < P:
                    print(i+1)
                    break
    elif rank_length < limit:
        if rank_list[-1] > P:
            print(rank_length+1)
        else:
            for i,v in enumerate(rank_list):
                if v == P:
                    print(i+1)
                    break
                elif v < P:
                    print(i+1)
                    break