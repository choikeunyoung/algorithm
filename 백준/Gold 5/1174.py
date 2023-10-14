import sys

sys.setrecursionlimit(10000)

def search_num(current, value):
    global cnt
    if current > 10:
        print(-1)
        exit()
    if cnt == N:
        if cnt > 11:
            print(int(value)-1)
        else:
            print(value)
        exit()
    if current == 1:
        cnt += 1
        if value == "9":
            search_num(current+1, str(int(value)+1))
        else:
            search_num(current, str(int(value)+1))
    else:
        flag = 0
        if value == "10":
            search_num(current, str(int(value)+1))
        else:
            for i in range(current-1):
                if int(value[i]) <= int(value[i+1]):
                    flag = 1
                    index = i
                    break
            if flag != 1:
                cnt += 1
                search_num(current,str((int(value)+1))) 
            else:
                value = int(value[:index+1] + "0"*(current-index-1))
                value += 10**(current - index - 1)
                search_num(len(str(value)), str(value))


N = int(input())
cnt = 1
ans = []
search_num(1,"0")