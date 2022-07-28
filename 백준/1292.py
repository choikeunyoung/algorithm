A,B=map(int,input().split())

problem = str()

for i in range(1,B+1):
    problem+="".join(f"{str(i)} "*i)

new_list = list(map(int,problem.split()))
print(sum(new_list[A-1:B]))