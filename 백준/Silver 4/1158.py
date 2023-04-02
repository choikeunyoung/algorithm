N,K = map(int,input().split())
num_list = []
for i in range(1,N+1):
    num_list.append(i)

cnt = K
answer = []
check = 0
while len(answer) != N:
    check_len = len(num_list)
    if check_len == 1:
        answer.append(num_list[-1])
    else:
        if cnt > check_len:
            cnt -= check_len
        else:
            cnt -= 1
            answer.append(num_list[cnt])
            del num_list[cnt]
            cnt += K
print("<", end="")
for i in answer:
    if i == answer[-1]:
        print(i,end="")
    else:
        print(i,end=", ")
print(">")