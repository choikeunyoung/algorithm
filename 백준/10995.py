T = int(input())
list = []
star_list=[]
if T % 2 == 0:
    star_list = "* "*(T*T)
else:
    print("* "*(T*T))
k = 0
cnt = 0
for i in range(T):
    for j in range(k,k+3):
        print(star_list[cnt:cnt+1],end="")
        
    print()
    k = j