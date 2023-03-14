N,M = map(int,input().split())

basket = [0]*N

for _ in range(M):
    i,j,k = map(int,input().split())
    insert_basket = [k]*(j-i+1)
    basket[i-1:j] = insert_basket
print(*basket)