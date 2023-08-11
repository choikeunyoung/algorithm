N = int(input())

num_list = list(map(int,input().split()))

answer = []

for i,v in enumerate(num_list):
    base_pos = len(answer)
    if answer:
        if v >= base_pos:
            answer.insert(0,i+1)
        else:
            answer.insert(base_pos-v, i+1)
    else:
        answer.append(i + 1)
print(*answer)