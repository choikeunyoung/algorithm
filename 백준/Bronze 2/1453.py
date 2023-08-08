N = int(input())

dict = {}
go_home=0
seat = list(map(int,input().split()))
for i in seat:
    if i in dict:
        go_home+=1
    else:
        dict[i] = 1
print(go_home)