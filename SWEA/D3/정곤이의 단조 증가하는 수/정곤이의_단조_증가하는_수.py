T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    ans_list = set()
    for i in range(N-1):
        for j in range(i+1,N):
            ans_list.add(num_list[i] * num_list[j])
    
    max_value = 0
    
    for k in ans_list:
        k = str(k)
        stack = []
        for l in k:
            if stack:
                if int(l) >= stack[-1]:
                    stack.append(int(l))
                else:
                    break
            else:
                stack.append(int(l))
        else:
            if max_value < int(k):
                max_value = int(k)
    if max_value == 0:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {max_value}")