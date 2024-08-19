N, K = map(int,input().split())

one_pos = 9
pos = 1
ans = 0
while K > one_pos*pos:
    K -= pos*one_pos
    ans += one_pos
    one_pos *= 10
    pos += 1
ans += ((K-1)//pos)+1
if ans > N:
    print(-1)
else:
    print(str(ans)[(K-1)%pos])