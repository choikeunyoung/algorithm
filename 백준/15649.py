from itertools import permutations

def perm(num,check):
    num_list = [1,2,3,4,5,6,7,8]
    return list(permutations(num_list[:num],check))

n,m = map(int,input().split())

result = perm(n,m)

for i in result:
    for j in i:
        print(j,end=" ")
    print()