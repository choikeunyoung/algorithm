T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    
    answer_list = []
    
    cnt = 0
    
    while True:
        answer_list.append(num_list.pop(-1))
        cnt += 1
        answer_list.append(num_list.pop(0))
        cnt += 1
        if cnt == 10:
            break
    ans = ""
    for answer in answer_list:
        ans += str(answer)+" "
    ans = ans.strip()
    print(f"#{tc} {ans}")